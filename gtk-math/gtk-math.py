#!/usr/bin/env python
#coding=utf-8

import gtk
import gobject
import os
import random

class GtkMath():
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("gtk-math.xml")
        
        self.window = self.builder.get_object("window")
        
        self.var1 = self.builder.get_object("var1")
        self.var2 = self.builder.get_object("var2")
        self.operation = self.builder.get_object("operation")
        self.percent = self.builder.get_object("percent")
        self.right_label = self.builder.get_object("right_label")
        self.wrong_label = self.builder.get_object("wrong_label")
        self.timer_button = self.builder.get_object("timer_button")
        self.timer_spinbutton = self.builder.get_object("timer_spinbutton")

        self.min = 0 # min. value to calc
        self.max = 10 #max. value to calc
        self.total = 0 #total calculations
        self.wrong = 0 #nr. of mistakes
        self.right = 0 #nr. if right calc
        self.builder.connect_signals(self)
        
        self.var1.set_text(str(random.randint(self.min, self.max) ))
        self.var2.set_text(str(random.randint(self.min, self.max) ))
        self.timer = gobject.timeout_add(2*1000, self.hide)
        
        self.window.show()

    def on_refresh_button_clicked(self, widget):
        #reset values
        self.min = 0
        self.max = 10
        self.total = 0
        self.wrong = 0
        self.right = 0
        
        self.right_label.set_text(str(self.right))
        self.wrong_label.set_text(str(self.wrong))
        self.percent.set_text("0%")
        self.var1.set_text(str(random.randint(self.min, self.max) ))
        self.var2.set_text(str(random.randint(self.min, self.max) ))
 
    def gtk_main_quit(widget, event):
        gtk.main_quit()
    
    def on_max_spin_value_changed(self, widget):
        self.max = int(widget.get_text())

    def on_min_spin_value_changed(self, widget):
        self.min = int(widget.get_text())

    def hide(self):
        self.var1.hide()
        self.var2.hide()
        #stop timer
        return False

    def on_answere_entry_activate(self, widget):
        gobject.source_remove(self.timer)
        answere = widget.get_text()
        
        if not answere.isdigit():
            widget.set_text("")
            return True
        
        if int(self.var1.get_text()) + int(self.var2.get_text()) == int(answere):
            print "OK"
            self.right += 1
            self.right_label.set_text(str(self.right))
        else:
            print "NOT OK"
            self.wrong += 1
            self.wrong_label.set_text(str(self.wrong))
            self.total += 1
            self.percent.set_text("%0.0f%%" %(self.right/float(self.total)*100.0))
            widget.set_text("")
            #IF toggle button set!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
            self.timer = gobject.timeout_add(2*1000, self.hide)
            #in case they were hidden
            self.var1.show()
            self.var2.show()

            return
        
        self.total += 1
        print self.min, self.max
        self.var1.set_text(str(random.randint(self.min, self.max) ))
        self.var2.set_text(str(random.randint(self.min, self.max) ))
        self.percent.set_text("%0.0f%%" %(self.right/float(self.total)*100.0))
        widget.set_text("")
        widget.grab_focus()
        #IF timout togglebutton set!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.timer = gobject.timeout_add(2*1000, self.hide)
        #in case they were hidden
        self.var1.show()
        self.var2.show()

if __name__ == "__main__":
    app = GtkMath()
    gtk.main()


