import random as r
import time
from tkinter import *
import Spaceship as M
from Intersection import *


class asteroid():
    def __init__(self, canvas, spaceship):
        from math import sin, cos, radians
        self.canvas = canvas
        self.spaceship = M.spaceship(canvas)
        self.vectors = list(range(-2, 2))
        self.angle = 0
        colors = ['gray40', 'gray50', 'gray60', 'gray70', 'gray75', 'gray80', 'gray90']
        # pointsbad = [r.randint(20, 50), r.randint(20, 40),  # 1
        #           r.randint(-50, 10), r.randint(40, 50),  # 2
        #           r.randint(-40, -10), r.randint(-10, 30),  # 3
        #           r.randint(-50, -30), r.randint(-50, -30),  # 4
        #           r.randint(-10, 20), r.randint(-50, -30),  # 5
        #           r.randint(30, 40), r.randint(-50, -40),  # 6
        #           r.randint(0, 50), r.randint(-10, 10)]  # 7
        # self.points = list(map(lambda x: x // 2, points))
        self.points = [r.randint(10, 50) * cos(radians(self.angle + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 0 + r.randint(-15, 15))),
                       r.randint(10, 50) * cos(radians(self.angle + 60 + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 60 + r.randint(-15, 15))),
                       r.randint(10, 50) * cos(radians(self.angle + 120 + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 120 + r.randint(-15, 15))),
                       r.randint(10, 50) * cos(radians(self.angle + 180 + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 180 + r.randint(-15, 15))),
                       r.randint(10, 50) * cos(radians(self.angle + 240 + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 240 + r.randint(-15, 15))),
                       r.randint(10, 50) * cos(radians(self.angle + 300 + r.randint(-15, 15))),
                       r.randint(10, 50) * sin(radians(self.angle + 300 + r.randint(-15, 15)))]
        self.points=list(map(lambda x: int(round(x)), self.points))
        self.id = self.canvas.create_polygon(self.points, fill=r.choices(colors), width=2)
        self.x = r.choice(self.vectors)
        self.y = r.choice(self.vectors)
        self.canvas_height = self.canvas.winfo_height()
        self.speed = 1
        self.speedlimit = 4
        self.canvas.move(self.id, r.randint(100, 900), r.randint(100, 900))

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        posx = pos[0::2]
        posy = pos[1::2]
        self.angle += r.randint(-10, 10)
        if min(posx) <= 0:
            self.x = 1 * abs(self.x) + r.randint(-self.speed, self.speed)
        if min(posy) <= 0:
            self.y = 1 * abs(self.y) + r.randint(-self.speed, self.speed)
        if max(posx) >= self.canvas_height:
            self.x = -1 * abs(self.x) + r.randint(-self.speed, self.speed)
        if max(posy) >= self.canvas_height:
            self.y = -1 * abs(self.x) + r.randint(-self.speed, self.speed)
        if self.x > self.speedlimit:
            self.x -= r.randint(1, self.speed)
        if self.x < -self.speedlimit:
            self.x += r.randint(1, self.speed)
        if self.y > self.speedlimit:
            self.y -= r.randint(1, self.speed)
        if self.y < -self.speedlimit:
            self.y += r.randint(1, self.speed)

    def hit(self, polygon):
        for i in range(6):
            for j in range(6):
                if intersection(self.points[i:i + 4] + polygon.points[j:j + 4]):
                    print('BANG!')
                    break
            break

    def __del__(self):
        self.canvas.itemconfigure(self.id, fill="Grey17")
        self.canvas.delete(self.id)
        del self


if __name__ == "__main__":

    tk = Tk()
    tk.title('Test')
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=1000, height=1000, bd=0, bg="Grey17", highlightthickness=0)
    canvas.pack()
    tk.update()

    a = asteroid(canvas, 1)
    b = asteroid(canvas, 1)
    c = asteroid(canvas, 1)
    print(a.points)

    tstart = time.time()
    flag = True
    while 1:
        a.draw()
        if time.time() - tstart > 5 and flag:
            print('Yes')
            tstart = time.time()
            del b
            # canvas.delete(b)
            # b=None
            flag = False
        elif flag:
            b.draw()
        else:
            c.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        canvas.delete(a)