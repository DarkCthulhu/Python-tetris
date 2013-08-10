#!/usr/bin/python
# -*- coding: utf-8 -*-

###
import pygame


###

"""
Count FPS using PyGame
"""

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    background = background.convert()
    screen.blit(background, (0, 0))
    
    mainloop = True
    while mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                mainloop = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False 
    
    
        clock = pygame.time.Clock()
        clock.tick(30)
        write_text(clock.get_fps(), screen)
        pygame.display.flip()

def write_text(message, surface):
    font = pygame.font.SysFont('mono', 20, bold=True)
    text_output = font.render(message, True, (255, 0, 0))
    surface.blit(text_output, (10, 10))
    

if __name__ == '__main__':

    # call with width of window and fps
    main()
