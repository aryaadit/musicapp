import pyaudio
import wave
import sys
import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *


# Window defaults
numCols = 5
numRows = 5
btnWidth = 6
btnHeight = btnWidth * 5

# Scrollbar object for canvas
class AutoScrollbar(Scrollbar):
    # A scrollbar that hides itself if it's not needed.
    # Only works if you use the grid geometry manager!
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")
    def place(self, **kw):
        raise TclError("cannot use place with this widget")

# Helper functions for mouse scroll binding
def on_vertical(event):
    canvas.yview_scroll(-1 * event.delta, 'units')

def on_horizontal(event):
    canvas.xview_scroll(-1 * event.delta, 'units')

# Create the window and the visual components
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Music App")
window.geometry("800x600")
window.maxsize(screen_width, screen_height)
window.minsize(200, 200)


# Vertical and horizontal scrollbar initialization
vscrollbar = AutoScrollbar(window, orient=VERTICAL)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(window, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(window, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)

vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

# Binding the mousewheel to scrollbars
canvas.bind_all('<MouseWheel>', on_vertical)
canvas.bind_all('<Shift-MouseWheel>', on_horizontal)

# Resize canvas to fit Frame size
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create canvas contents and Frame
frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

# Style to allow resizing of buttons
s=ttk.Style()
s.theme_use('clam')
s.configure('bb.TButton', background = 'white', padding = btnHeight)

# Inserting widgets into the Frame
for i in range(numRows):
    for j in range(numCols):
        counter = i*numCols+j+1
        btn_pres = ttk.Button(frame, text = "Clip " + str(counter), width = btnWidth, style = 'bb.TButton').grid(row = i, column = j)

# Finalize the canvas details
canvas.create_window(0, 0, anchor=NW, window=frame)
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
# canvas.pack(fill=BOTH, expand=YES)
# frame.pack(fill=BOTH, expand=YES)


# Run the program
window.mainloop()
