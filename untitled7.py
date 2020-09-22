# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:11:01 2020

@author: CALVIN
"""


import pygame
BLACK = (0,0,0)
WHITE = (225,225,225)
pygame.init()
size = (700,500)
screen = pygame.display.set_caption('my game')
done = False
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT():
            done = True
    screen.fill(WHITE)
    pygame.draw.circle(screen,BLACK,(100,100),20)
    pygame.display.flip()
    pygame.draw.circle(screen,BLACK,(100,140),20)
    pygame.display.flip()
    pygame.draw.circle(screen,BLACK,(140,100),20)
    pygame.display.flip()
    pygame.draw.circle(screen,BLACK,(140,140),20)
    pygame.display.flip()
pygame.quit()