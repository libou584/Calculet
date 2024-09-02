import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import src.background as bg


def main() :
    width = 368
    height = 528
    x = 1920 - width
    y = 1080 - height
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

    queue, program, pixels_buffer = bg.create_context(width, height)
    
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
        pixels = bg.run_kernel(queue, program, pixels_buffer, width, height, time)
        surface = pygame.image.frombuffer(pixels.tobytes(), (width, height), 'RGBA')
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
