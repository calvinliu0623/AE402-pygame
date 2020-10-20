# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:19:50 2020

@author: CALVIN
"""


import random
import pygame
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("走動的方塊")

done = False
click = False
Rcount = 0
Rlimit = 50


clock = pygame.time.Clock()



while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()
            click = True
        elif keys [pygame.K_SPACE]:
            x = random.randint(0,400)
            y = random.randint(0,400)
        else:
            pass

    screen.fill(WHITE)
    if click and Rcount < Rlimit:
        pygame.draw.circle(screen,RED,a,Rcount)
        Rcount+=1
        if Rcount >= Rlimit:
            click = False
    pygame.display.flip()

    clock.tick(60)
pygame.quit()