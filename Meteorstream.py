import random as r
import time
from tkinter import *
from Asteroid import *


class meteorstream():
    def __init__(self, canvas, num):
        self.canvas = canvas
        self.num = num
        self.stream = [asteroid(self.canvas, 1) for x in range(self.num)]

    def draw(self):
        for i in self.stream:
            i.draw()


if __name__ == "__main__":

    tk = Tk()
    tk.title('Test')
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=1000, height=1000, bd=0, bg="Grey17", highlightthickness=0)
    canvas.pack()
    tk.update()

    g = meteorstream(canvas, 10)
    tstart = time.time()
    while 1:
        g.draw()
        if time.time() - tstart > 5:
            print('Yes')
            tstart = time.time()
            canvas.delete(g.stream[-1])
            g.stream.pop()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
