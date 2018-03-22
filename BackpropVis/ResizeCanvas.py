"""
Adapted for python3  and with some modifications
from Steven Vascellero's solution on Stack Overflow:
https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
"""

from tkinter import *


# a subclass of Canvas for dealing with resizing of windows
class ResizeCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


if __name__ == "__main__":
    root = Tk()
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=YES)
    canvas = ResizeCanvas(frame, width=850, height=400, bg="red", highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    canvas.create_line(0, 0, 200, 100)
    canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    canvas.create_rectangle(50, 25, 150, 75, fill="blue")

    # tag all of the drawn widgets
    canvas.addtag_all("all")
    root.mainloop()
