import pygame
from ui import menu
from racer import run_game
from persistence import save_score, load_leaderboard

pygame.init()

screen = pygame.display.set_mode((400,600))

while True:
    choice = menu(screen)

    if choice == "play":
        username = input("Enter your name: ")
        result = run_game(screen, username)

        if result:
            save_score(result)

    elif choice == "leaderboard":
        data = load_leaderboard()
        screen.fill((255,255,255))
        y = 50
        for i, d in enumerate(data):
            text = f"{i+1}. {d['name']} - {d['score']}"
            img = pygame.font.SysFont(None,30).render(text, True, (0,0,0))
            screen.blit(img, (50,y))
            y += 30
        pygame.display.flip()
        pygame.time.wait(3000)

    elif choice == "quit":
        break