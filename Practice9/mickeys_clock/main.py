import pygame
from clock import MickeyClock


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Mickey's Clock")

    fps_clock = pygame.time.Clock()
    app = MickeyClock(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        app.draw()
        pygame.display.flip()
        fps_clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()