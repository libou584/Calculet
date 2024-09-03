import pygame


class Button :
    def __init__(self, x, y, width, height, type) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type

    def draw(self, screen) :
        s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        s.fill((255, 255, 255, 80))
        screen.blit(s, (self.x, self.y))
    
    def is_clicked(self, x, y) :
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


def loadButtons() :
    buttons = []
    buttons.append(Button(32, 176, 64, 64, "%"))
    buttons.append(Button(32, 256, 64, 64, "^"))
    buttons.append(Button(32, 336, 64, 64, "exp"))
    buttons.append(Button(32, 416, 64, 64, "!"))
    buttons.append(Button(32, 496, 64, 64, "("))
    buttons.append(Button(112, 176, 64, 64, "+"))
    buttons.append(Button(112, 256, 64, 64, "7"))
    buttons.append(Button(112, 336, 64, 64, "4"))
    buttons.append(Button(112, 416, 64, 64, "1"))
    buttons.append(Button(112, 496, 64, 64, ")"))
    buttons.append(Button(192, 176, 64, 64, "-"))
    buttons.append(Button(192, 256, 64, 64, "8"))
    buttons.append(Button(192, 336, 64, 64, "5"))
    buttons.append(Button(192, 416, 64, 64, "2"))
    buttons.append(Button(192, 496, 64, 64, "0"))
    buttons.append(Button(272, 176, 64, 64, "x"))
    buttons.append(Button(272, 256, 64, 64, "9"))
    buttons.append(Button(272, 336, 64, 64, "6"))
    buttons.append(Button(272, 416, 64, 64, "3"))
    buttons.append(Button(272, 496, 64, 64, "."))
    buttons.append(Button(352, 176, 64, 64, "/"))
    buttons.append(Button(352, 256, 64, 64, "AC"))
    buttons.append(Button(352, 336, 64, 64, "<-"))
    buttons.append(Button(352, 416, 64, 144, "="))
    return buttons


def drawButtons(screen, buttons) :
    for button in buttons :
        button.draw(screen)
