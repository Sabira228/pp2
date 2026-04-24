import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (20, 0)

food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))

score = 0
level = 1
speed = 5

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # ---------------- WRAP AROUND (НОВОЕ) ----------------
    head = (head[0] % WIDTH, head[1] % HEIGHT)

    snake.insert(0, head)

    # Self collision (осталась смерть только от себя)
    if head in snake[1:]:
        running = False

    # Eating food
    if head == food:
        score += 1

        # Level up
        if score % 3 == 0:
            level += 1
            speed += 2

        # Generate new food NOT on snake
        while True:
            food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))
            if food not in snake:
                break
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 200, 0), (*segment, 20, 20))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))

    # UI
    text = font.render(f"Score: {score}  Level: {level}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()