#!/usr/bin/env python
#coding=utf-8

import gtk
import gnomeapplet

def sample_factory(applet, iid):
    label = gtk.Label("Success!")
    applet.add(label)

    applet.show_all()
    return gtk.TRUE

gnomeapplet.bonobo_factory("OAFIID:GNOME_PysampleApplet_Factory", gnomeapplet.Applet.__gtype__,
        "hello", "0", sample_factory)


