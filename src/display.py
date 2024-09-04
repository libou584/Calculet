import pygame
import numpy as np


class Display :
    def __init__(self, top, bottom, font) :
        self.top = top
        self.bottom = bottom
        self.font = font
    
    def draw(self, screen) :
        s = pygame.Surface((384, 128), pygame.SRCALPHA)
        s.fill((255, 255, 255, 130))
        screen.blit(s, (32, 32))

        top_text_surface = self.font.render(self.top, True, (0, 0, 0))
        screen.blit(top_text_surface, (52, 48))
        
        bottom_text_surface = self.font.render(self.bottom, True, (0, 0, 0))
        bottom_text_rect = bottom_text_surface.get_rect(bottomright=(396, 144))
        screen.blit(bottom_text_surface, bottom_text_rect)
    
    def update(self, type) :
        if type is None :
            return None
        if type == "=" :
            if self.top == "" :
                try :
                    if self.bottom != "" :
                        strValid = getValid(self.bottom)
                        res = getRes(strValid)
                        self.top = strValid
                        self.bottom = res
                except :
                    self.top = "Not valid"
        else :
            if self.top != "" and self.top != "Not valid" :
                self.bottom = ""
            self.top = ""
        
            if type == "AC" :
                self.top = ""
                self.bottom = ""
            elif type == "<-" :
                self.bottom = self.bottom[:-1]
            elif type == "^" :
                self.bottom += "**("
            elif type == "exp" :
                self.bottom += "exp("
            elif type == "x" :
                self.bottom += "*"
            elif type == "!" :
                self.bottom += "fact("
            else :
                self.bottom += type


def getValid(s) :
    n = 0
    for c in s :
        if c == "(" :
            n += 1
        elif c == ")" :
            n -= 1
    if n > 0 :
        return s + ")" * n
    if n < 0 :
        return "(" * -n + s
    return s


def getRes(strValid) :
    prompt = """def fact(n):
    return prod(range(1, n+1))

result = """ + strValid
    local_namespace = {}
    exec(prompt, {"__builtins__": {"range": range}, "prod": np.prod, "exp": np.exp}, local_namespace)
    res = local_namespace['result']
    if res > 10**10 or (res < 10**-10 and res > 0) or res < -10**10 or (res > -10**-10 and res < 0) :
        return f"{res:.4e}"
    return str(round(res, 4))