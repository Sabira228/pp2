import pygame
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# ---------------- SETTINGS ----------------
drawing = False
mode = "pencil"
color = BLACK
brush_size = 5

start_pos = None
last_pos = None

# text tool
text_mode = False
text_input = ""
text_pos = (0, 0)
font = pygame.font.SysFont(None, 28)

# ---------------- FLOOD FILL ----------------
def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]
    while stack:
        px, py = stack.pop()

        if px < 0 or px >= WIDTH or py < 0 or py >= HEIGHT:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        stack.append((px+1, py))
        stack.append((px-1, py))
        stack.append((px, py+1))
        stack.append((px, py-1))


running = True
while running:
    screen.fill(WHITE)
    temp_surface = canvas.copy()  # для preview

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------------- MOUSE DOWN ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            last_pos = event.pos

            if mode == "fill":
                flood_fill(canvas, *event.pos, color)

            elif mode == "text":
                text_mode = True
                text_input = ""
                text_pos = event.pos

            else:
                drawing = True

        # ---------------- MOUSE UP ----------------
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "line":
                pygame.draw.line(canvas, color, start_pos, end_pos, brush_size)

            elif mode == "rect":
                pygame.draw.rect(canvas, color,
                                 (*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), brush_size)

            elif mode == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

            elif mode == "square":
                side = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(canvas, color, (*start_pos, side, side), brush_size)

            elif mode == "right_triangle":
                points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                pygame.draw.polygon(canvas, color, points, brush_size)

            elif mode == "equilateral_triangle":
                side = abs(end_pos[0]-start_pos[0])
                height = side * math.sqrt(3)/2
                points = [
                    start_pos,
                    (start_pos[0]+side, start_pos[1]),
                    (start_pos[0]+side/2, start_pos[1]-height)
                ]
                pygame.draw.polygon(canvas, color, points, brush_size)

            elif mode == "rhombus":
                cx = (start_pos[0]+end_pos[0])//2
                cy = (start_pos[1]+end_pos[1])//2
                points = [(cx,start_pos[1]), (end_pos[0],cy),
                          (cx,end_pos[1]), (start_pos[0],cy)]
                pygame.draw.polygon(canvas, color, points, brush_size)

        # ---------------- KEYBOARD ----------------
        if event.type == pygame.KEYDOWN:

            # режимы
            if event.key == pygame.K_p: mode = "pencil"
            if event.key == pygame.K_l: mode = "line"
            if event.key == pygame.K_r: mode = "rect"
            if event.key == pygame.K_c: mode = "circle"
            if event.key == pygame.K_s: mode = "square"
            if event.key == pygame.K_t: mode = "right_triangle"
            if event.key == pygame.K_y: mode = "equilateral_triangle"
            if event.key == pygame.K_h: mode = "rhombus"
            if event.key == pygame.K_f: mode = "fill"
            if event.key == pygame.K_x: mode = "text"

            # brush size
            if event.key == pygame.K_1: brush_size = 2
            if event.key == pygame.K_2: brush_size = 5
            if event.key == pygame.K_3: brush_size = 10

            # цвета
            if event.key == pygame.K_q: color = (255,0,0)
            if event.key == pygame.K_w: color = (0,255,0)
            if event.key == pygame.K_e: color = (0,0,255)

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # text typing
            if text_mode:
                if event.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    canvas.blit(img, text_pos)
                    text_mode = False
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

    # ---------------- DRAWING ----------------
    if drawing and mode == "pencil":
        current_pos = pygame.mouse.get_pos()
        pygame.draw.line(canvas, color, last_pos, current_pos, brush_size)
        last_pos = current_pos

    # ---------------- PREVIEW ----------------
    if drawing and mode in ["line","rect","circle","square","right_triangle","equilateral_triangle","rhombus"]:
        end_pos = pygame.mouse.get_pos()

        if mode == "line":
            pygame.draw.line(temp_surface, color, start_pos, end_pos, brush_size)

        elif mode == "rect":
            pygame.draw.rect(temp_surface, color,
                             (*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), brush_size)

        elif mode == "circle":
            radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(temp_surface, color, start_pos, radius, brush_size)

        elif mode == "square":
            side = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
            pygame.draw.rect(temp_surface, color, (*start_pos, side, side), brush_size)

        elif mode == "right_triangle":
            points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
            pygame.draw.polygon(temp_surface, color, points, brush_size)

        elif mode == "equilateral_triangle":
            side = abs(end_pos[0]-start_pos[0])
            height = side * math.sqrt(3)/2
            points = [start_pos,(start_pos[0]+side,start_pos[1]),
                      (start_pos[0]+side/2,start_pos[1]-height)]
            pygame.draw.polygon(temp_surface, color, points, brush_size)

        elif mode == "rhombus":
            cx = (start_pos[0]+end_pos[0])//2
            cy = (start_pos[1]+end_pos[1])//2
            points = [(cx,start_pos[1]), (end_pos[0],cy),
                      (cx,end_pos[1]), (start_pos[0],cy)]
            pygame.draw.polygon(temp_surface, color, points, brush_size)

    # ---------------- TEXT PREVIEW ----------------
    if text_mode:
        preview = font.render(text_input, True, color)
        temp_surface.blit(preview, text_pos)

    screen.blit(temp_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()