import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# ---------------- IMAGES ----------------
car_img = pygame.image.load("car.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")

car_img = pygame.transform.scale(car_img, (40, 60))
enemy_img = pygame.transform.scale(enemy_img, (40, 60))
coin_img = pygame.transform.scale(coin_img, (30, 30))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ---------------- PLAYER ----------------
player = car_img.get_rect()
player.center = (180, 500)

# ---------------- ENEMY ----------------
enemy = enemy_img.get_rect()
enemy.x = random.randint(0, WIDTH - 40)
enemy.y = 0

# ---------------- COIN ----------------
coin = coin_img.get_rect()
coin.x = random.randint(0, WIDTH - 30)
coin.y = random.randint(-300, -50)

speed = 5
coin_count = 0

font = pygame.font.SysFont(None, 30)

game_over = False

while True:

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:

        # ---------------- PLAYER MOVE ----------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.x < WIDTH - 40:
            player.x += 5

        # ---------------- ENEMY MOVE ----------------
        enemy.y += speed
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - 40)

        # ---------------- COIN MOVE ----------------
        coin.y += speed
        if coin.y > HEIGHT:
            coin.y = random.randint(-300, -50)
            coin.x = random.randint(0, WIDTH - 30)

        # ---------------- COIN COLLISION ----------------
        if player.colliderect(coin):
            coin_count += 1
            coin.y = random.randint(-300, -50)
            coin.x = random.randint(0, WIDTH - 30)

        # ---------------- ENEMY COLLISION (GAME OVER) ----------------
        if player.colliderect(enemy):
            game_over = True

        # ---------------- DRAW ----------------
        screen.blit(car_img, player)
        screen.blit(enemy_img, enemy)
        screen.blit(coin_img, coin)

        text = font.render(f"Coins: {coin_count}", True, BLACK)
        screen.blit(text, (250, 10))

    else:
        # GAME OVER SCREEN
        text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Coins: {coin_count}", True, BLACK)

        screen.blit(text, (130, 250))
        screen.blit(score_text, (140, 300))

    pygame.display.flip()
    clock.tick(60)