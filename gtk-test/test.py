#!/usr/bin/env python
#coding=utf-8

import gtk
import os



class test_label:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("destroy", lambda w: gtk.main_quit() )

        label = gtk.Label()
        label.set_text("TEST")
        label.show()
        label2 = gtk.Label()
        label2.set_text("TEST2")
        label2.show()
        eventbox = gtk.EventBox()
        eventbox.add(label)
        eventbox.connect("enter_notify_event", self.show_entry)
        eventbox.show()
        self.vbox = gtk.VBox(2)
        self.vbox.add(eventbox)
        self.vbox.add(label2)
        self.vbox.show()
        window.add(self.vbox)
        window.show()
    
    def show_entry(self, w, e):
        print w, e
        wpopup = gtk.Window(gtk.WINDOW_POPUP)
        gtk.
        self.entry = gtk.Entry()
        wpopup.add(self.entry)
        wpopup.grab_focus()
        wpopup.show_all()

if __name__ == "__main__":
    app = test_label()
    gtk.main()
