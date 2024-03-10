
import scenes
import sys
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *
import math
import common

sceneList= {"None":None}
defaultScene = "menu"

started = True
pygame.init()

MAX_FPS = 0
clock = pygame.time.Clock()

width, height = 900,700
screen = pygame.display.set_mode((width,height),pygame.HWACCEL,32)


def set_started(value):
    global started
    started = value

def get_started():
    return started

def load_scenes():
    print("Compiling scenes...")
    scenePath = os.getcwd()+"/scenes/"
    for x in os.listdir(scenePath):
        sceneReader = open(scenePath+x)
        sceneData = sceneReader.read()
        sceneReader.close()
        sceneName = x.removesuffix(".py")
        sceneCode = compile(sceneData,sceneName,"exec")
        sceneList[sceneName] = sceneCode
        print("Compiled scene", sceneName)
    common.currentScene = defaultScene

load_scenes()

pygame.font.init() 

font = pygame.font.SysFont('Segoe UI', 24)

center = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)

def switch_scene(newScene):
    common.currentScene = newScene
    common.started = False

while common.running:
    if common.loadedScene != common.currentScene:
        common.started = False
        common.loadedScene = common.currentScene
        print("Loading scene",common.loadedScene)
    else: 
        common.deltaTime = clock.tick(MAX_FPS)
        common.timer+=common.deltaTime
        common.events = pygame.event.get()
        for event in common.events:
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
                sys.exit()
                quit()
        exec(sceneList[common.loadedScene],globals(),locals())

server.start()
client.start()
