import sys
import os
sys.path.append(os.getcwd())
from main import *
from pygame.locals import *
import pygame
from hutils import *

defaultColor = pygame.color.Color(25,25,75)
defaultHoverColor = pygame.color.Color(125,145,190)
defaultOutlineColor = pygame.color.Color(0,0,0)
defaultOutlineHoverColor = pygame.color.Color(255,255,255)

defaultTextColor = pygame.color.Color(255,255,255)
defaultTextHoverColor = pygame.color.Color(0,0,0)

class Button:    
    def __init__(self,label,position,size,function = None,color = defaultColor,textColor = defaultTextColor, textHoverColor = defaultTextHoverColor, hoverColor = defaultHoverColor, borderSmooth = 0, outlineSize = 0, outlineColor = defaultOutlineColor, outlineHoverColor = defaultOutlineHoverColor):
        self.label = label
        self.function = function
        self.position = position
        self.size = size
        self.color = color
        self.textColor = textColor,
        self.textHoverColor = textHoverColor
        self.finalTextColor = textColor
        self.hoverColor = hoverColor
        self.finalColor = defaultColor
        self.borderSmooth = borderSmooth
        self.outlineSize = outlineSize
        self.outlineColor = outlineColor
        self.outlineHoverColor = outlineHoverColor
        self.finalOutlineColor = outlineColor
        self.canClick = True
        self.clickScale =0.8
        self.scale = 1
        

    def draw(self,deltaTime):
        
        mousePos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.position.x-self.size.x/2,self.position.y-self.size.y/2 ,self.size.x,self.size.y)
        finalRect = rect.scale_by(self.scale,self.scale)
        collide = rect.collidepoint(mousePos)
   
   
        if collide:
            self.finalOutlineColor = pygame.color.Color.lerp(self.finalOutlineColor,self.outlineHoverColor,max(0,min(deltaTime*0.040,1)))
            self.finalColor = pygame.color.Color.lerp(self.finalColor,self.hoverColor,max(0,min(deltaTime*0.033,1)))
            self.finalTextColor = pygame.color.Color.lerp(self.finalTextColor,self.textHoverColor,max(0,min(deltaTime*0.033,1)))
            clickUp = False
            clickDown = False
            for event in common.events:
                if event.type == pygame.MOUSEBUTTONUP:
                    clickUp = True
                    if self.canClick:
                        self.canClick = False
                        exec(self.function,globals(), locals())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clickDown = True
                else:
                 self.canClick = True
            if clickDown:
                self.scale = self.clickScale
            else:
                self.scale = lerp(self.scale,1.15,deltaTime*0.05)
                
                


        else:
            self.scale = lerp(self.scale,1.0,deltaTime*0.05)
            self.canClick = True
            self.finalOutlineColor = pygame.color.Color.lerp(self.finalOutlineColor,self.outlineColor,max(0,min(deltaTime*0.040,1)))
            self.finalTextColor = pygame.color.Color.lerp(self.finalTextColor,self.textColor,max(0,min(deltaTime*0.033,1)))
            self.finalColor = pygame.color.Color.lerp(self.finalColor,self.color,max(0,min(deltaTime*0.033,1)))
        if self.outlineSize!=0:
            aspectRatio = self.size.x/self.size.y 
            scalingX = (self.outlineSize+1)
            scalingY = (self.outlineSize+1)
            pygame.draw.rect(screen,self.finalOutlineColor,finalRect.inflate((scalingX,scalingY)),0,self.borderSmooth)
        pygame.draw.rect(screen,self.finalColor,finalRect,0,self.borderSmooth)
        label = font.render(self.label, True, self.finalTextColor)
        text_rect = label.get_rect(center=(self.position.x,self.position.y))
        screen.blit(label, text_rect)
   


