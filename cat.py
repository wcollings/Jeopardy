#generic category class
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import windows

class Category:
    def __init__(self, name):
        self.vbox=Gtk.VBox(spacing=6)
        self.Title=Gtk.Label(str(name))
        self.vbox.pack_start(self.Title, True, True, 0)
        self.vals=[i for i in range(100,600,100) ]
        self.Buttons= [Gtk.ToggleButton() for i in range(5)]
        print(name)
        for i,j in zip(self.Buttons, self.vals):
            i.set_label(str(j))
            i._value=self.Title.get_text()+":"+str(j)
            i.connect("toggled", windows.on_click)
            self.vbox.pack_start(i, True, True, 0)
