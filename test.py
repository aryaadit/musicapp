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
# for i in range(numRows):
#     for j in range(numCols):
#         print("Creating buttons")
#         counter = i*numCols+j+1
#         text = "Clip " + str(counter)
#         btn_pres = ttk.Button(frame, text = text, width = btnWidth)
#         btn_pres['style'] = 'bb.TButton'
#         btn_pres['command'] = lambda: playClip(counter)
#         btn_pres.grid(row = i, column = j)

print("Finished making buttons")
btn_clip1 = ttk.Button(frame, text = "Clip 1", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(1)).grid(row = 1, column = 1)
btn_clip2 = ttk.Button(frame, text = "Clip 2", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(2)).grid(row = 1, column = 2)
btn_clip3 = ttk.Button(frame, text = "Clip 3", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(3)).grid(row = 1, column = 3)
btn_clip4 = ttk.Button(frame, text = "Clip 4", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(4)).grid(row = 1, column = 4)
btn_clip5 = ttk.Button(frame, text = "Clip 5", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(5)).grid(row = 1, column = 5)
btn_clip6 = ttk.Button(frame, text = "Clip 6", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(6)).grid(row = 2, column = 1)
btn_clip7 = ttk.Button(frame, text = "Clip 7", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(7)).grid(row = 2, column = 2)
btn_clip8 = ttk.Button(frame, text = "Clip 8", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(8)).grid(row = 2, column = 3)
btn_clip9 = ttk.Button(frame, text = "Clip 9", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(9)).grid(row = 2, column = 4)
btn_clip10 = ttk.Button(frame, text = "Clip 10", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(10)).grid(row = 2, column = 5)
btn_clip11 = ttk.Button(frame, text = "Clip 11", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(11)).grid(row = 3, column = 1)
btn_clip12 = ttk.Button(frame, text = "Clip 12", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(12)).grid(row = 3, column = 2)
btn_clip13 = ttk.Button(frame, text = "Clip 13", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(13)).grid(row = 3, column = 3)
btn_clip14 = ttk.Button(frame, text = "Clip 14", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(14)).grid(row = 3, column = 4)
btn_clip15 = ttk.Button(frame, text = "Clip 15", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(15)).grid(row = 3, column = 5)
btn_clip16 = ttk.Button(frame, text = "Clip 16", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(16)).grid(row = 4, column = 1)
btn_clip17 = ttk.Button(frame, text = "Clip 17", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(17)).grid(row = 4, column = 2)
btn_clip18 = ttk.Button(frame, text = "Clip 18", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(18)).grid(row = 4, column = 3)
btn_clip19 = ttk.Button(frame, text = "Clip 19", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(19)).grid(row = 4, column = 4)
btn_clip20 = ttk.Button(frame, text = "Clip 20", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(20)).grid(row = 4, column = 5)
btn_clip21 = ttk.Button(frame, text = "Clip 21", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(21)).grid(row = 5, column = 1)
btn_clip22 = ttk.Button(frame, text = "Clip 22", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(22)).grid(row = 5, column = 2)
btn_clip23 = ttk.Button(frame, text = "Clip 23", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(23)).grid(row = 5, column = 3)
btn_clip24 = ttk.Button(frame, text = "Clip 24", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(24)).grid(row = 5, column = 4)
btn_clip25 = ttk.Button(frame, text = "Clip 25", width = btnWidth,style = 'bb.TButton',command = lambda: playClip(25)).grid(row = 5, column = 5)



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
