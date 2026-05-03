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

coin_value = 1  # вес монеты (по умолчанию)

# ---------------- GAME VARIABLES ----------------
speed = 5
coin_count = 0

font = pygame.font.SysFont(None, 30)

game_over = False


# функция для случайного веса монеты
def random_coin():
    global coin_value
    coin.x = random.randint(0, WIDTH - 30)
    coin.y = random.randint(-300, -50)

    # случайный вес монеты
    coin_value = random.choice([1, 3, 5])


# вызываем первый раз
random_coin()

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
            random_coin()

        # ---------------- COIN COLLISION ----------------
        if player.colliderect(coin):
            coin_count += coin_value  # добавляем вес монеты
            random_coin()

        # ---------------- SPEED INCREASE ----------------
        # каждые 5 монет увеличиваем скорость
        speed = 5 + (coin_count // 5)

        # ---------------- ENEMY COLLISION ----------------
        if player.colliderect(enemy):
            game_over = True

        # ---------------- DRAW ----------------
        screen.blit(car_img, player)
        screen.blit(enemy_img, enemy)

        # меняем цвет монеты в зависимости от веса
        if coin_value == 1:
            tint = (255, 255, 0)  # жёлтая
        elif coin_value == 3:
            tint = (0, 255, 0)    # зелёная
        else:
            tint = (255, 0, 0)    # красная

        colored_coin = coin_img.copy()
        colored_coin.fill(tint, special_flags=pygame.BLEND_MULT)

        screen.blit(colored_coin, coin)

        # текст
        text = font.render(f"Coins: {coin_count}", True, BLACK)
        speed_text = font.render(f"Speed: {speed}", True, BLACK)

        screen.blit(text, (250, 10))
        screen.blit(speed_text, (10, 10))

    else:
        # ---------------- GAME OVER SCREEN ----------------
        text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Coins: {coin_count}", True, BLACK)

        screen.blit(text, (130, 250))
        screen.blit(score_text, (140, 300))

    pygame.display.flip()
    clock.tick(60)