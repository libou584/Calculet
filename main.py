import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import src.background as bg
import src.button as bt


def main() :
    width = 448
    height = 592
    x = 1920 - width
    y = 1080 - height
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

    queue, program, pixels_buffer = bg.create_context(width, height)

    buttons = bt.loadButtons()
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Calculet")
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        

        time = pygame.time.get_ticks() / 1000.0
        bg.run_kernel(queue, program, pixels_buffer, width, height, time, screen)
        bt.drawButtons(screen, buttons)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
