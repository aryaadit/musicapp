import pyaudio
import wave
import sys
import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *


# Global defaults
numCols = 5
numRows = 5
btnWidth = 6
btnHeight = btnWidth * 5
CHUNK = 1024

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

def playClip(x):
    print("In play clip for some dumbass reason")
    if(x == 1):
        wf = wave.open("test1.wav", 'rb')
    elif(x == 2):
        wf = wave.open("Closed-Hi-Hat-1.wav", 'rb')
    else:
        wf = wave.open("Alesis-Fusion-Voice-Oohs-C4.wav", 'rb')

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

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
        print("Creating buttons")
        counter = i*numCols+j+1
        text = "Clip " + str(counter)
        btn_pres = ttk.Button(frame, text = text, width = btnWidth)
        btn_pres['style'] = 'bb.TButton'
        # btn_pres['command'] = playClip(counter)
        btn_pres.grid(row = i, column = j)

btn_test = ttk.Button(frame, text = "TEST BUTTON", width = btnWidth)

# Finalize the canvas details
canvas.create_window(0, 0, anchor=NW, window=frame)
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the program
window.mainloop()



# if len(sys.argv) < 1:
#     print("Insuffcient parameters provided")
#     sys.exit(-1)


# while(True):
#     x = raw_input('Enter Audio Key: ')
#
#     # wf = wave.open(sys.argv[1], 'rb')
#     # print sys.argv[1]
#
#     if(x == 'a'):
#         wf = wave.open("test1.wav", 'rb')
#     elif(x == 'b'):
#         wf = wave.open("Closed-Hi-Hat-1.wav", 'rb')
#     else:
#         wf = wave.open("Alesis-Fusion-Voice-Oohs-C4.wav", 'rb')
#
#
#
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
#
#     data = wf.readframes(CHUNK)
#
#     while data != '':
#         stream.write(data)
#         data = wf.readframes(CHUNK)
#
#     stream.stop_stream()
#     stream.close()
#
# p.terminate()
