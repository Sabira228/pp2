import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)

canvas = pygame.Surface((600, 400))
canvas.fill(WHITE)

drawing = False
mode = "draw"
color = (0, 0, 0)

start_pos = None

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse up (рисуем фигуры)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                pygame.draw.rect(canvas, color,
                                 (*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))

            elif mode == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius)

        # keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_d:
                mode = "draw"

            # colors
            if event.key == pygame.K_1:
                color = (255, 0, 0)
            if event.key == pygame.K_2:
                color = (0, 255, 0)
            if event.key == pygame.K_3:
                color = (0, 0, 255)

    # ---------------- DRAWING ----------------
    if drawing:
        x, y = pygame.mouse.get_pos()

        if mode == "draw":
            pygame.draw.circle(canvas, color, (x, y), 5)

        elif mode == "eraser":
            pygame.draw.circle(canvas, WHITE, (x, y), 10)

    # ---------------- SHOW CANVAS ----------------
    screen.blit(canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()