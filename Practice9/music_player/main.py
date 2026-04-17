import pygame
from player import MusicPlayer


def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 400))
    pygame.display.set_caption("Music Player")

    fps_clock = pygame.time.Clock()
    player = MusicPlayer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        player.draw(screen)
        pygame.display.flip()
        fps_clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()