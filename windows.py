import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import data


#objects pertaining to Question
H_Label=Gtk.Label("X for X")

stack=Gtk.Stack()
stack_sw=Gtk.StackSwitcher()
stack_sw.set_stack(stack)

#question body setup
Q_Label=Gtk.Label()
Q_Label.set_line_wrap(True)
stack.add_titled(Q_Label, "q", "Question")

#question answer setup
A_Label=Gtk.Label()
A_Label.set_line_wrap(True)
stack.add_titled(A_Label, "a", "Answer")

back=Gtk.Button("Go back")

Question=Gtk.Grid()
Question.set_column_homogeneous(True)
Question.set_row_homogeneous(True)
Question.attach(stack_sw,17,0,20,10)
Question.attach(H_Label, 0,10,40,10)
Question.attach(stack,5,20,30,80)
Question.attach(back,0,100,40,10)


#various other things we need. Our main window, and a board
Board=Gtk.VBox(spacing=6)
win=Gtk.Window()
win.connect("destroy", Gtk.main_quit)

#Going to a question
def on_click(widget):
    global Q_Label
    global A_Label
    back.connect("clicked", on_return)
    #each button has its category name and packed into a field called "_value". Unpack it for future use
    words=widget._value.split(":")
    
    #parse through the questions dataset and find the right question
    Q_Label.set_text(data.questions[str(words[0])][str(words[1])])
    
    #parse through the answers dataset and select the right answer
    A_Label.set_text(data.answers[str(words[0])][str(words[1])])
    
    #set the label at the top
    H_Label.set_text(str(words[0])+" for " + str(words[1]))
    
    #hide the board, and throw up the question window
    win.remove(Board)
    win.add(Question)
    Question.show_all()

#coming back from a question
def on_return(widget):
    #hide the question window, and throw up the board again
    win.remove(Question)
    win.add(Board)
    #make sure the next time you go to a question it doesn't show the answer first
    stack.set_visible_child(Q_Label)

