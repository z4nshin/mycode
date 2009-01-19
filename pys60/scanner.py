import appuifw
#Get wlantools of the net
import wlantools
import e32
import audio

#experimental code to start learning python on S60

s=u""
timer = e32.Ao_timer()
say = audio.Sound.open(u'e:\\Python\secure.mp3')

def scan():
	hosts = wlantools.scan()
	s=u""
	for i in hosts:
		if i['SecurityMode']=="Open":
			say.play()
			audio.say(u"network found" + i['SSID'])
			s=s+i['SSID']+u"\n"
			appuifw.note(s, 'info')
	timer.after(120, scan)


appuifw.app.title = u"Scanner"
timer.after(5,scan)
#no gracefull exit as of yet :(

