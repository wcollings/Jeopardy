import gi
from cat import Category
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import windows

class window:
    Cols=list()
    cats=Gtk.HBox(spacing=6)
    nameList={"concepts","standards","bugs","random"}
    def __init__(self):
        self.Cols= [Category(str(i)) for i in self.nameList]
        self.cats.set_homogeneous(True)
        for e in self.Cols:
            print(e.Title.get_text())
            self.cats.pack_start(e.vbox, False, True,0)
def main():
    main=window()
    windows.Board=main.cats
    windows.win.add(windows.Board)
    windows.win.show_all()
    Gtk.main()

if __name__=="__main__":
    main()
