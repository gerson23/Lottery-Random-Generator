#!/usr/bin/env python

import pygtk, gtk
from generator import *

class Interface:
    def hello(self, widget, data=None):
        print "bazinga"

    def loto(self, widget, data=None):
        print "generating lucky numbers..."
        if data != None:
            numbers = globals()[data]()
        numbers.sort()
        if self.state != "mega_sena" and data == "mega_sena":
            self.string += "Luck numbers for MEGA-SENA:\t"
        elif self.state != "quina" and data == "quina":
            self.string += "Luck numbers for QUINA:\t\t"
        elif self.state != "dupla_sena" and data == "dupla_sena":
            self.string += "Luck numbers for DUPLA-SENA:\t"
        elif self.string != "loto_facil" and data == "loto_facil":
            self.string += "Luck numbers for LOTO-FACIL:\t"
        elif self.string != "lotomania" and data == "lotomania":
            self.string += "Luck numbers for LOTOMANIA:\t"
        else:
            self.string += "\t\t\t\t\t\t\t\t\t"
        for no in numbers:
            self.string = self.string + str(no) + " "   
        self.textbuffer.set_text(self.string)
        self.string = self.string + "\n"
        self.state = data

    def clear(self, widget, data=None):
        self.string = ""
        self.status = ""
        self.textbuffer.set_text(self.string)

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return false

    def menuitem_response(self, widget, data=None):
        return false

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.state = ""
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

        '''buttons start here'''
        button = gtk.Button("Clear")
        button.connect("clicked", self.clear, None)
        vbox.pack_start(button, False, False, 0)
        button.show()

        button = gtk.Button("Mega-Sena")
        button.connect("clicked", self.loto, "mega_sena")
        hbox.pack_start(button, False, False, 0)
        button.show()

        button = gtk.Button("Quina")
        button.connect("clicked", self.loto, "quina")
        hbox.pack_start(button, False, False, 0)
        button.show()

        button = gtk.Button("Loto-facil")
        button.connect("clicked", self.loto, "loto_facil")
        hbox.pack_start(button, False, False, 0)
        button.show()

        button = gtk.Button("Lotomania")
        button.connect("clicked", self.loto, "lotomania")
        hbox.pack_start(button, False, False, 0)
        button.show()

        button = gtk.Button("Dupla-Sena")
        button.connect("clicked", self.loto, "dupla_sena")
        hbox.pack_start(button, False, False, 0)
        button.show()

        self.button = gtk.Button("Exit")
        self.button.connect("clicked", self.hello, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        vbox.pack_start(self.button, False, False, 0)
        self.button.show()
        '''end buttons'''

        '''menu start here
        file_menu = gtk.Menu()

        save_item = gtk.MenuItem("Save")
        quit_item = gtk.MenuItem("Quit")

        file_menu.append(save_item)
        file_menu.append(quit_item)
        save_item.connect_object("activate", self.menuitem_response, "self.save")
        quit_item.connect_object("activate", gtk.Widget.destroy, "self.destroy")

        save_item.show()
        quit_item.show()

        menu_bar = gtk.MenuBar()
        self.window.add(menu_bar)
        menu_bar.show()
        file_item = gtk.MenuItem("File")
        file_item.show()
        file_item.set_submenu(file_item)
        menu_bar.append(file_menu)'''

        self.window.show()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    hello = Interface()
    hello.main()
