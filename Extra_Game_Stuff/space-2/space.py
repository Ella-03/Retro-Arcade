#!/usr/bin/python3
#Ella Adam
#4/09/2021

'''Followed a tutorial from "Tech With Tim" ---> https://www.youtube.com/watch?v=Q-__8Xw9KTM '''

import pygame
import os
import random
import time

pygame.font.init()
pygame.init()


screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Space Shooters")


#Colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

#Images

'''
red_ship = pygame.image.load(os.path.join("img", "red-ship.png"))
blue_ship = pygame.image.load(os.path.join("img", "blue-ship.png"))
green_ship = pygame.image.load(os.path.join("img", "green-ship.png"))
player_ship = pygame.image.load(os.path.join("img", "player-ship.png"))

red_laser = pygame.image.load(os.path.join("img", "red-laser.png"))
blue_laser = pygame.image.load(os.path.join("img", "blue-laser.png"))
green_laser = pygame.image.load(os.path.join("img", "green-laser.png"))
yellow_laser = pygame.image.load(os.path.join("img", "yellow-laser.png"))

'''
#Ships
red_ship = pygame.image.load(os.path.join("red-ship.png"))
blue_ship = pygame.image.load(os.path.join("blue-ship.png"))
green_ship = pygame.image.load(os.path.join("green-ship.png"))
player_ship = pygame.image.load(os.path.join("player-ship.png"))

#Lasers
red_laser = pygame.image.load(os.path.join("red-laser.png"))
blue_laser = pygame.image.load(os.path.join("blue-laser.png"))
green_laser = pygame.image.load(os.path.join("green-laser.png"))
yellow_laser = pygame.image.load(os.path.join("yellow-laser.png"))


def main():
    
    start = True
    FPS = 60
    clock = pygame.time.Clock()
    
    
    # -------- Main Program Loop -----------
    
    def redraw_win():
        pygame.display.update()
    
    
    while start:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                start = False # Flag that we are done so we exit this loop
            elif event.type == pygame.K_ESCAPE:
                quit()   
            '''
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE: #Pressing the ESC Key will quit the game
                    screen_width=800
                    screen_height=600
                    screen=pygame.display.set_mode((screen_width, screen_height))
                    pygame.mixer.music.load('Music/Platformer2.mp3')
                    pygame.mixer.music.play()                    
                    game_library()            
            '''
            
    # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(BLACK)




#Initialize the Game

main()
pygame.quit()
quit()
