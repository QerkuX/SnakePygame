import pygame as py
from random import randint

py.init()
#they must be divisible by gs (grid size)!
WW = 1000 #window width
WH = 1000 #window height

win = py.display.set_mode((WW, WH))
py.display.set_caption("Snake")
clock = py.time.Clock()
font = py.font.SysFont('calibri', 30)
mg = (30, 30, 30) #map gray
mb = (10, 10, 10) #map black
FPS = 6

sx = [0] #snake X
sy = [0] #snake Y
se = 1 #snake elements
sw = 50 #snake width
sh = 50 #snake height
sc = (0, 200, 0) #snake color
hc = (0, 255, 0) #snakes head color
xsm = 0 #X speed multiplier
ysm = 0 #Y speed multiplier
gs = 50 #grid square size

#insert snake with fruit I:
fx = WW / 2
fy = WW / 2
fc = (255, 0, 0)
fw = 50
fh = 50

#Are buttons pressed
ap = False
dp = False
wp = False
sp = False

score = 0

run = True
while run:

    #exit button
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    #map grid pattern
    for i in range(1, int((WH / gs) + 1)):
        for j in range(1, int((WW / gs) + 1)):
            if (j + i) % 2 == 0:
                py.draw.rect(win, mg, (j * 50 - 50, i * 50 - 50, sw, sh))
            else:
                py.draw.rect(win, mb, (j * 50 - 50, i * 50 - 50, sw, sh))

    #moving system
    keys = py.key.get_pressed()

    if keys[py.K_a]:
        if xsm == 0 and not ap:
            xsm = -1
            ysm = 0
            ap = True
    else:
        ap = False
    if keys[py.K_d]:
        if xsm == 0 and not dp:
            xsm = 1
            ysm = 0
            dp = True
    else:
        dp = False
    if keys[py.K_w]:
        if ysm == 0 and not wp:
            ysm = -1
            xsm = 0
            wp = True
    else:
        wp = False
    if keys[py.K_s]:
        if ysm == 0 and not sp:
            ysm = 1
            xsm = 0
            sp = True
    else:
        sp = False


    #Updating snake position
    if se > 1:
        for i in range(se-1 , 0, -1):
            sx[i] = sx[i-1]
            sy[i] = sy[i-1]
            py.draw.rect(win, sc, (sx[i], sy[i], sw, sh))

    sx[0] += gs * xsm
    sy[0] += gs * ysm
    py.draw.rect(win, hc, (sx[0], sy[0], sw, sh))

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
                if sx[i] == fx and sy[i] == fy:
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
