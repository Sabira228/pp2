import pygame
import math  # нужен для равностороннего треугольника

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)

# Холст, на котором рисуем
canvas = pygame.Surface((600, 400))
canvas.fill(WHITE)

drawing = False  # зажата ли кнопка мыши
mode = "draw"    # текущий режим рисования
color = (0, 0, 0)

start_pos = None  # начальная точка фигуры

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажали кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Отпустили кнопку мыши → рисуем фигуру
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            # ---------- ПРЯМОУГОЛЬНИК ----------
            if mode == "rect":
                pygame.draw.rect(canvas, color,
                                 (x1, y1, x2 - x1, y2 - y1))

            # ---------- КРУГ ----------
            elif mode == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, radius)

            # ---------- КВАДРАТ ----------
            elif mode == "square":
                side = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color,
                                 (x1, y1, side, side))

            # ---------- ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК ----------
            elif mode == "right_triangle":
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(canvas, color, points)

            # ---------- РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК ----------
            elif mode == "equilateral_triangle":
                side = abs(x2 - x1)
                height = side * math.sqrt(3) / 2

                points = [
                    (x1, y1),
                    (x1 + side, y1),
                    (x1 + side / 2, y1 - height)
                ]
                pygame.draw.polygon(canvas, color, points)

            # ---------- РОМБ ----------
            elif mode == "rhombus":
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                points = [
                    (cx, y1),
                    (x2, cy),
                    (cx, y2),
                    (x1, cy)
                ]
                pygame.draw.polygon(canvas, color, points)

        # ---------- КЛАВИАТУРА ----------
        if event.type == pygame.KEYDOWN:

            # режимы рисования
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_s:
                mode = "square"
            if event.key == pygame.K_t:
                mode = "right_triangle"
            if event.key == pygame.K_y:
                mode = "equilateral_triangle"
            if event.key == pygame.K_h:
                mode = "rhombus"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_d:
                mode = "draw"

            # цвета
            if event.key == pygame.K_1:
                color = (255, 0, 0)
            if event.key == pygame.K_2:
                color = (0, 255, 0)
            if event.key == pygame.K_3:
                color = (0, 0, 255)

    # ---------- РИСОВАНИЕ КИСТЬЮ ----------
    if drawing:
        x, y = pygame.mouse.get_pos()

        if mode == "draw":
            pygame.draw.circle(canvas, color, (x, y), 5)

        elif mode == "eraser":
            pygame.draw.circle(canvas, WHITE, (x, y), 10)

    # ---------- ОТРИСОВКА ----------
    screen.blit(canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()