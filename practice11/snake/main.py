import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# ---------------- SNAKE ----------------
snake = [(100, 100)]
direction = (20, 0)

# ---------------- FOOD ----------------
food = (0, 0)
food_value = 1       # вес еды
food_timer = 0       # сколько времени осталось

# ---------------- GAME ----------------
score = 0
level = 1
speed = 5

font = pygame.font.SysFont(None, 30)


# функция генерации еды
def spawn_food():
    global food, food_value, food_timer

    # случайная позиция не на змейке
    while True:
        food = (random.randrange(0, WIDTH, 20),
                random.randrange(0, HEIGHT, 20))
        if food not in snake:
            break

    # случайный вес еды
    food_value = random.choice([1, 2, 3])

    # таймер (в кадрах)
    food_timer = random.randint(100, 300)


# первый спавн
spawn_food()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------- CONTROLS ----------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    # ---------------- MOVE ----------------
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # телепорт через стенки
    head = (head[0] % WIDTH, head[1] % HEIGHT)

    snake.insert(0, head)

    # ---------------- COLLISION WITH SELF ----------------
    if head in snake[1:]:
        running = False

    # ---------------- FOOD TIMER ----------------
    food_timer -= 1
    if food_timer <= 0:
        spawn_food()  # еда исчезла и появилась новая

    # ---------------- EAT FOOD ----------------
    if head == food:
        score += food_value

        # уровень и скорость
        if score % 3 == 0:
            level += 1
            speed += 1

        spawn_food()
    else:
        snake.pop()

    # ---------------- DRAW SNAKE ----------------
    for segment in snake:
        pygame.draw.rect(screen, (0, 200, 0), (*segment, 20, 20))

    # ---------------- DRAW FOOD ----------------
    # цвет зависит от веса
    if food_value == 1:
        color = (255, 0, 0)      # красный
    elif food_value == 2:
        color = (255, 165, 0)    # оранжевый
    else:
        color = (0, 0, 255)      # синий

    pygame.draw.rect(screen, color, (*food, 20, 20))

    # ---------------- UI ----------------
    text = font.render(f"Score: {score}  Level: {level}", True, (0, 0, 0))
    timer_text = font.render(f"Food time: {food_timer}", True, (0, 0, 0))

    screen.blit(text, (10, 10))
    screen.blit(timer_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()