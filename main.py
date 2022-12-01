import pygame as py
from random import randint

py.init()
WW = 800 #window width
WH = 800 #window height
win = py.display.set_mode((WW, WH))
py.display.set_caption("Snake")
clock = py.time.Clock()
font = py.font.SysFont('calibri', 30)
FPS = 8

sx = [0] #snake X
sy = [0] #snake Y
se = 1 #snake elements
sw = 50 #snake width
sh = 50 #snake height
sc = (0, 255, 0) #snake color
xsm = 0 #X speed multiplier
ysm = 0 #Y speed multiplier
gs = 50 #grid square size

#insert snake with fruit I:
fx = WW / 2
fy = WW / 2
fc = (255, 0, 0)
fw = 50
fh = 50

score = 0
run = True
while run:

    #exit button
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    win.fill((0, 0, 0))

    #moving system
    keys = py.key.get_pressed()

    if keys[py.K_a]:
        xsm = -1
        ysm = 0
    if keys[py.K_d]:
        xsm = 1
        ysm = 0
    if keys[py.K_w]:
        ysm = -1
        xsm = 0
    if keys[py.K_s]:
        ysm = 1
        xsm = 0

    #Updating snake position
    if se > 1:
        for i in range(se-1 , 0, -1):
            sx[i] = sx[i-1]
            sy[i] = sy[i-1]
            py.draw.rect(win, sc, (sx[i], sy[i], sw, sh))

    sx[0] += gs * xsm
    sy[0] += gs * ysm
    py.draw.rect(win, sc, (sx[0], sy[0], sw, sh))

    #snake collision detection
    if se > 1:
        for i in range(se):
            for j in range(se):
                if sx[i] == sx[j] and sy[i] == sy[j] and not i == j:
                    run = False


    #fruit check
    if sx[0] == fx and sy[0] == fy:
        sx.append(sx[se-1])
        sy.append(sy[se-1])
        se += 1
        score += 1

        #generate new fruit
        while True:
            fx = randint(0, (WW-fw) / gs) * gs
            fy = randint(0, (WH-fh) / gs) * gs
            for i in range(se):
                if sx[0] == fx and sy[0] == fy:
                    continue
            break

    py.draw.rect(win, fc, (fx, fy, fw, fh))
    label = font.render("score: " + str(score), 1, (255, 255, 255))
    win.blit(label, (0, 0))
    #wall collision detecion
    if sx[0] > WW - sw or sx[0] < 0 or sy[0] > WH - sh or sy[0] < 0:
        run = False

    py.display.update()
    clock.tick(FPS)