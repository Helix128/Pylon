import sys
import os
sys.path.append(os.getcwd())
import math
import main
from hgui import * 
import inspect
import hutils
import common



def start():
    if common.started == True:
        return
    else:
        common.started = True
        init_scene()

def on_switch():
    main.switch_scene("template")
    return 0

def init_scene():
    global btn
    btn = Button("Switch",pygame.Vector2(center.x,center.y),pygame.Vector2(128,32))
    btn.function = on_switch.__code__
    btn.outlineSize = 4
    btn.borderSmooth = 4
    return 0

def update():
   
    return 0

def draw():
    screen.fill((int(127+math.sin(common.timer*0.01)*32),110,120))
    return 0



def drawGUI():
    btn.draw(common.deltaTime)
    return 0

def render():
    draw()
    drawGUI()
    pygame.display.flip()

start()
update()
render()