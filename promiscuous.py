import sys, struct, fcntl
from socket import *
#import socket

SIOCGIFFLAGS = 0x8913
SIOCSIFFLAGS = 0x8914
SIOCGIFHWADDR = 0x8927
SIOCGIFINDEX = 0x8933

SOCK_PACKET = 10
SOL_PACKET = 263

PACKET_ADD_MEMBERSHIP = 1
PACKET_DROP_MEMBERSHIP = 2

PACKET_MR_MULTICAST = 0
PACKET_MR_PROMISC = 1
PACKET_MR_ALLMULTI = 2

ETH_P_ALL = 0x3
ETH_P_IP = 0x800
ETH_P_ARP = 0x806
ETH_P_RARP = 0x8035

#sizes in bytes
ETHER_SIZE = 14
IP_SIZE = 20
IP_OPTIONS = 4

class MySocket(socket):
	def __init__(self, family, type, proto=0, _sock=None):
		socket.__init__(self, family, type, proto, _sock)
		self.SIOCGIFFLAGS = None

	def promiscuous(self, dev="eth0",on=False ):
		fileno = self.fileno()
		result = fcntl.ioctl(fileno, SIOCGIFFLAGS, struct.pack("16s16x",dev))
		(devname, flags)= struct.unpack("16sH14x", result)
		if on == True:
			if (flags & 256) != 256:
				print "ON"
				flags = flags | 256
				self.SIOCGIFFLAGS = struct.unpack("16sH14x", \
					fcntl.ioctl(fileno, SIOCSIFFLAGS,struct.pack("16sH14x",devname, flags)) )
		else:
			if (flags & 256) != 0:
				print "OFF", flags & 256
				flags = flags ^ 256
				self.SIOCGIFFLAGS = struct.unpack("16sH14x", \
					fcntl.ioctl(fileno, SIOCSIFFLAGS,struct.pack("16sH14x",devname, flags)) )

	def pass_all_packets(self, dev="eth0"):
		fileno = self.fileno()
		result = struct.unpack("16si12x", fcntl.ioctl(fileno, SIOCGIFINDEX, struct.pack("16s16x",dev)))
		#print result

		#not sure if this line is needed!!!!!!!!!!!!!!!!!!!!!!!1
		#self.setsockopt(SOL_PACKET,PACKET_ADD_MEMBERSHIP, struct.pack("iH10x",result[1],PACKET_MR_PROMISC) )
		
		#bind socket to an interface and open it for all packets
		self.bind((dev, ETH_P_ALL, PACKET_OTHERHOST, 1))

def get_ether_layer(packet):
	a1 = struct.unpack("6B",packet[:6])
	a2 = struct.unpack("6B",packet[6:12])
	p = struct.unpack("H",packet[12:14])
	#convert to ntohs/ntol?????????????????????
	return {"dest":(a1[0],a1[1],a1[2],a1[3],a1[4],a1[5]), "src":(a2[0],a2[1],a2[2],a2[3],a2[4],a2[5]),
		"proto":ntohs(p[0]) }

def get_ip_layer(packet):
	i = ntohl(struct.unpack("I", packet[14:18])[0])
	i2 = ntohl(struct.unpack("I", packet[18:22])[0])
	i3 = ntohl(struct.unpack("I", packet[22:26])[0])
	i4 = ntohl(struct.unpack("I", packet[26:30])[0])
	i5 = ntohl(struct.unpack("I", packet[30:34])[0])
	
	options = None
	version = i >> 28 & 0x0F
	hdrlen = i >> 24 & 0x0F
	if hdrlen > 5:
		i5 = ntohl(struct.unpack("I", packet[34:38])[0])
		print "OPTIONS!!!!!!"
		options = i5
	total_length = i  & 0x0000FFFF
	ident = i2 & 0xFFFF0000
	flags = i2 >> 13 & 3
	frag_offset = i2 & 0x1FFF
	ttl = i3 >> 24 & 0xFF
	proto = i3 >> 16 & 0xFF
	chksum = i3 & 0xFFFF

	src_ip = [ (i4 >> c*8) & 0xFF for c in range(0,4) ]
	src_ip.append(i4)
	dst_ip = [ (i5 >> c*8) & 0xFF for c in range(0,4) ]
	dst_ip.append(i5)
	#src_ip.reverse()
	#dst_ip.reverse()
	
	#check checksum, has to be 0xFFFF
	sum = 0
	for a in [i,i2,i3,i4,i5]:
		sum += (a) & 0xFFFF
		a = a >> 16
		sum += (a) & 0xFFFF
	carry = (sum >> 16) & 0xFFFF
	sum += carry
	sum = sum & 0xFFFF
	if sum != 0xFFFF:
		raise "Checksum Error"

	return {"version":version, "hdrlen":hdrlen, "total_length":total_length,
		"indent":ident, "flags":flags, "frag_offset":frag_offset,
		"ttl":ttl, "proto":proto, "chksum":chksum, "src_ip":src_ip, "dst_ip":dst_ip,
		"options":options}


#s = MySocket(AF_INET, SOCK_PACKET, ETH_P_ALL)
s = MySocket(PF_PACKET, SOCK_RAW, ETH_P_ALL)
s.promiscuous("wlan0", True)
s.pass_all_packets("wlan0") 
#s.bind(("wlan0", ETH_P_ALL, PACKET_OTHERHOST, 1))
while True:
	r = s.recv(1024)
	#print r
	eth = get_ether_layer(r)
	print "dest addres: %X:%x:%x:%x:%x:%x" % eth['dest']
	print "source hwaddres: %X:%x:%x:%x:%x:%x" % eth['src']
	print "proto: 0x%x" % eth['proto']
	if eth['proto'] == 0x800:
		ip = get_ip_layer(r)
		print ip
		if ip['proto'] == 0x6:
			print "TCP", ntohl(struct.unpack("I", r[34:38])[0]) >> 16 & 0xFFFF
			print "TCP", ntohl(struct.unpack("I", r[34:38])[0]) & 0xFFFF
			data = ntohl(struct.unpack("I", r[46:50])[0]) >> 28 & 0xF
			print data
			print r[34+data*4:]

	print "-"*80
