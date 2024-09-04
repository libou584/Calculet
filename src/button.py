import pygame


class Button :
    def __init__(self, x, y, width, height, type, font) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.font = font
        self.hoveredLastFrame = False

    def draw(self, screen, x, y, sounds) :
        s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.type == "AC" or self.type == "=" :
            s.fill((255, 255, 255, 130))
        else :
            s.fill((255, 255, 255, 70))
        if self.mouseOver(x, y) :
            screen.blit(s, (self.x, self.y))
            if not self.hoveredLastFrame :
                sounds[1].play()
            self.hoveredLastFrame = True
        else :
            self.hoveredLastFrame = False
        text_surface = self.font.render(self.type, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        s.blit(text_surface, text_rect)
        screen.blit(s, (self.x, self.y))
    
    def mouseOver(self, x, y) :
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


def loadButtons(font) :
    buttons = []
    buttons.append(Button(32, 176, 64, 64, "%", font))
    buttons.append(Button(32, 256, 64, 64, "^", font))
    buttons.append(Button(32, 336, 64, 64, "exp", font))
    buttons.append(Button(32, 416, 64, 64, "!", font))
    buttons.append(Button(32, 496, 64, 64, "(", font))
    buttons.append(Button(112, 176, 64, 64, "+", font))
    buttons.append(Button(112, 256, 64, 64, "7", font))
    buttons.append(Button(112, 336, 64, 64, "4", font))
    buttons.append(Button(112, 416, 64, 64, "1", font))
    buttons.append(Button(112, 496, 64, 64, ")", font))
    buttons.append(Button(192, 176, 64, 64, "-", font))
    buttons.append(Button(192, 256, 64, 64, "8", font))
    buttons.append(Button(192, 336, 64, 64, "5", font))
    buttons.append(Button(192, 416, 64, 64, "2", font))
    buttons.append(Button(192, 496, 64, 64, "0", font))
    buttons.append(Button(272, 176, 64, 64, "x", font))
    buttons.append(Button(272, 256, 64, 64, "9", font))
    buttons.append(Button(272, 336, 64, 64, "6", font))
    buttons.append(Button(272, 416, 64, 64, "3", font))
    buttons.append(Button(272, 496, 64, 64, ".", font))
    buttons.append(Button(352, 176, 64, 64, "/", font))
    buttons.append(Button(352, 256, 64, 64, "AC", font))
    buttons.append(Button(352, 336, 64, 64, "<-", font))
    buttons.append(Button(352, 416, 64, 144, "=", font))
    return buttons


def drawButtons(screen, buttons, sounds) :
    x, y = pygame.mouse.get_pos()
    for button in buttons :
        button.draw(screen, x, y, sounds)
