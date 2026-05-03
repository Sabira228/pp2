import pygame

pygame.init()
font = pygame.font.SysFont(None, 40)

def draw_text(screen, text, x, y):
    img = font.render(text, True, (0,0,0))
    screen.blit(img, (x,y))

def menu(screen):
    while True:
        screen.fill((255,255,255))
        draw_text(screen, "1. Play", 150, 150)
        draw_text(screen, "2. Leaderboard", 150, 200)
        draw_text(screen, "3. Settings", 150, 250)
        draw_text(screen, "4. Quit", 150, 300)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return "play"
                if event.key == pygame.K_2: return "leaderboard"
                if event.key == pygame.K_3: return "settings"
                if event.key == pygame.K_4: return "quit"