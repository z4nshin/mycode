import btconsole
from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("192.168.2.2", 1025))
btconsole.run_with_redirected_io(sock,btconsole.interact, None, None, locals())
sock.close()

