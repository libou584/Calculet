import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import src.background as bg
import src.button as bt
import src.display as dp


def main() :

    width = 448
    height = 592
    x = 1920 - width
    y = 1080 - height
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
    project_path = os.environ['PROJECT_PATH']

    queue, program, pixels_buffer = bg.create_context(width, height)
    
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    font = pygame.font.Font(project_path + "Calculet/asset/font/futura.ttf", 24)
    sounds = [pygame.mixer.Sound(project_path + "Calculet/asset/sounds/click.wav"), pygame.mixer.Sound(project_path + "Calculet/asset/sounds/hover.wav")]
    sounds[0].set_volume(0.3)
    sounds[1].set_volume(0.1)

    buttons = bt.loadButtons(font)
    display = dp.Display("", "", font)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Calculet")
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                display.update(bt.buttonClicked(pygame.mouse.get_pos(), buttons, sounds))

        time = pygame.time.get_ticks() / 1000.0
        bg.run_kernel(queue, program, pixels_buffer, width, height, time, screen)
        bt.drawButtons(screen, buttons, sounds)
        display.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
