import pygame


class Display :
    def __init__(self, top, bottom) :
        self.top = top
        self.bottom = bottom
    
    def draw(self, screen) :
        s = pygame.Surface((384, 128), pygame.SRCALPHA)
        s.fill((255, 255, 255, 130))
        screen.blit(s, (32, 32))