#!/usr/bin/env python
#coding=utf-8


import imaplib
import getpass

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login("z4nshin@gmail.com", "!@#$%^&*")
m.select()
type, data = m.search(None, 'UNSEEN')
for mesg in data[0].split():
    stat, data =  m.fetch(mesg, '(BODY[HEADER])')
    try:
        index_from = data[0][1].index("From:")
        eol = data[0][1][index_from:].index("\n")
        print data[0][1][index_from:index_from+eol]
    except:
        pass
    try:    
        index_from = data[0][1].index("subject:")
        eol = data[0][1][index_from:].index("\n")
        print data[0][1][index_from:index_from+eol] 
    except:
        pass
