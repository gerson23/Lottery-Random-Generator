#!/usr/bin/env python

import pygtk, gtk
import generator

class Interface:
    def hello(self, widget, data=None):
        print "bazinga"

    def mega(self, widget, data=None):
        print "generating mega-sena..."
        numbers = generator.mega_sena()
        numbers.sort()
        for no in numbers:
            self.string = self.string + str(no) + " "   
        self.textbuffer.set_text(self.string)

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return false

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(0)
        self.window.resize(500, 300)
        self.window.set_title("Lottery Generator")

        box1 = gtk.VBox(False,0)
        self.window.add(box1)
        box1.show()

        box2 = gtk.VBox(False,10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        self.textview = gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        sw.add(self.textview)
        sw.show()
        self.textview.show()

        box2.pack_start(sw)
        self.string = ""
        self.textbuffer.set_text(self.string)
        hbox = gtk.HButtonBox()
        box2.pack_start(hbox, False, False, 0)
        hbox.show()

        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)

        self.button = gtk.Button("Exit")
        self.button.connect("clicked", self.hello, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        vbox.pack_start(self.button, False, False, 0)
        self.button.show()

        button = gtk.Button("Mega-Sena")
        button.connect("clicked", self.mega, None)
        vbox.pack_start(button, False, False, 0)
        button.show()

        self.window.show()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    hello = Interface()
    hello.main()
