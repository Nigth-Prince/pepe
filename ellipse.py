import math
import pygame as pg
# c = int(input()
c = 20
pg.init()
w,h = 1366,768
win = pg.display.set_mode((w,h))
f = 0
stop = 20
startup = True
def 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    win.fill((0,0,0))
    # pg.draw.rect(win,(100,100,100),(334,34,334*2,700))
    if f == 0 or f == 1:
        s = 1
    elif f == stop :
        stop += 1
        s = -1
    f += s
    # if not startup:
        # pg.draw.arc(win,(255,255,255),(0,0,600,600),0,15)
    for i in range(c):
        if i == 0 and startup:
            s_x = 300
            sstep = 0
            while 1:
                win.fill((0, 0, 0))
                pg.draw.arc(win, (255, 255, 255), (333+350 - sstep, 34, 0 + sstep * 2, 700), 0, 15)
                sstep += 1
                pg.display.update()
                pg.time.Clock().tick(30)
                if sstep == 350:
                    step = f * i
                    startup = False
                    break
        else:
            step = f * i
        if 600-step*2 > 0:

            pg.draw.arc(win,(255,255,255),(333,34+step,700,700-step*2),0,15)
            pg.draw.arc(win, (255, 255, 255), (333+step, 34, 700-step*2, 700), 0,15)
    #     # pg.draw.circle(win,(0,255,0),(150,150),step,1)
    pg.display.update()
    pg.time.Clock().tick(60)