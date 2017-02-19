import Tkinter as tk
from Tkinter import *
import ttk
import random

fortunes = [
    "2016 is your Lucky year!", "Good fortune is coming your way.",
    "Better stay in today", "Love is on the horizon",
    "Whatever will be will be.",
]

def tell_fortune(): #Update Label Text
    r = random.randint(0,4)
    result.set(fortunes[r])


window = Tk()
window.title("Fortune Teller")
window.geometry('400x200') # Fixed window Size 400, 200


mainframe = ttk.Frame(window, relief='groove', borderwidth=5, padding='12 12 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# img = PhotoImage(file='source.gif')


result = StringVar()
result.set('')

lbl_Header = ttk.Label(mainframe).grid(columnspan=3, row=0, sticky=(W,E))
lbl_fortune = ttk.Label(mainframe, textvariable=result).grid(columnspan=3, row=1)

pb = ttk.Progressbar(mainframe,orient='horizontal',length=300,mode='determinate', maximum=100, value=4).grid(columnspan=3,row=2, sticky=(W,E))

btn_press = ttk.Button(mainframe, width=30, text="Press Here", command=tell_fortune).grid(column=0, row=3, sticky=W)
btn_quit = ttk.Button(mainframe, text="Quit", command=exit).grid(column=1, row=3, stick=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


window.mainloop()

root = tk.Tk()

# Base size
normal_width = 1920
normal_height = 1080

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 10)
percentage_height = screen_height / (normal_height / 10)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2)

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size
fontsize = int(14 * scale_factor)
minimum_size = 8
if fontsize < minimum_size:
    fontsize = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

frame = ttk.Frame(root)
button = ttk.Button(frame, text="Test", style='New.TButton')

frame.grid(column=0, row=0)
button.grid(column=0, row=0)

root.mainloop()




# def data():
#     for i in range(50):
#        Label(frame,text=i).grid(row=i,column=0)
#        Label(frame,text="my text"+str(i)).grid(row=i,column=1)
#        Label(frame,text="..........").grid(row=i,column=2)
#
# def myfunction(event):
#     canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)
#
# root=Tk()
# sizex = 800
# sizey = 600
# posx  = 100
# posy  = 100
# root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
#
# myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
# myframe.place(x=10,y=10)
#
# canvas=Canvas(myframe)
# frame=Frame(canvas)
# myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
# canvas.configure(yscrollcommand=myscrollbar.set)
#
# myscrollbar.pack(side="right",fill="y")
# canvas.pack(side="left")
# canvas.create_window((0,0),window=frame,anchor='nw')
# frame.bind("<Configure>",myfunction)
# data()
# root.mainloop()

def on_vertical(event):
    canvas.yview_scroll(-1 * event.delta, 'units')

def on_horizontal(event):
    canvas.xview_scroll(-1 * event.delta, 'units')

root = Tk()
h = Scrollbar(root, orient=HORIZONTAL)
v = Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
canvas.grid(column=0, row=0, sticky=(N,W,E,S))

canvas.bind_all('<MouseWheel>', on_vertical)
canvas.bind_all('<Shift-MouseWheel>', on_horizontal)

h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()



# class AutoScrollbar(Scrollbar):
#     # A scrollbar that hides itself if it's not needed.
#     # Only works if you use the grid geometry manager!
#     def set(self, lo, hi):
#         if float(lo) <= 0.0 and float(hi) >= 1.0:
#             # grid_remove is currently missing from Tkinter!
#             self.tk.call("grid", "remove", self)
#         else:
#             self.grid()
#         Scrollbar.set(self, lo, hi)
#     def pack(self, **kw):
#         raise TclError("cannot use pack with this widget")
#     def place(self, **kw):
#         raise TclError("cannot use place with this widget")
#
#
# # create scrolled canvas
#
# root = Tk()
#
# vscrollbar = AutoScrollbar(root)
# vscrollbar.grid(row=0, column=1, sticky=N+S)
# hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
# hscrollbar.grid(row=1, column=0, sticky=E+W)
#
# canvas = Canvas(root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
# canvas.grid(row=0, column=0, sticky=N+S+E+W)
#
# vscrollbar.config(command=canvas.yview)
# hscrollbar.config(command=canvas.xview)
#
# # make the canvas expandable
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
#
# # create canvas contents
# frame = Frame(canvas)
# frame.rowconfigure(1, weight=1)
# frame.columnconfigure(1, weight=1)
#
# rows = 5
# for i in range(1, rows):
#     for j in range(1, 10):
#         button = Button(frame, text="%d, %d" % (i,j))
#         button.grid(row=i, column=j, sticky='news')
#
# canvas.create_window(0, 0, anchor=NW, window=frame)
# frame.update_idletasks()
# canvas.config(scrollregion=canvas.bbox("all"))
#
# root.mainloop()
