import pygame
import random
import time

WIDTH, HEIGHT = 400, 600

def run_game(screen, username):
    player = pygame.Rect(180, 500, 40, 60)
    speed = 5

    obstacles = []
    powerups = []

    coins = 0
    distance = 0

    active_power = None
    power_timer = 0

    clock = pygame.time.Clock()

    while True:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= 5
        if keys[pygame.K_RIGHT]: player.x += 5

        # ---------- SPAWN ----------
        if random.randint(1,30) == 1:
            obstacles.append(pygame.Rect(random.randint(0,360), -50, 40, 40))

        if random.randint(1,200) == 1:
            powerups.append({
                "rect": pygame.Rect(random.randint(0,360), -50, 30, 30),
                "type": random.choice(["nitro","shield","repair"]),
                "time": time.time()
            })

        # ---------- MOVE ----------
        for o in obstacles:
            o.y += speed

        for p in powerups:
            p["rect"].y += speed

        # ---------- COLLISIONS ----------
        for o in obstacles:
            if player.colliderect(o):
                if active_power == "shield":
                    active_power = None
                    obstacles.remove(o)
                else:
                    return {"name": username, "score": coins, "distance": distance}

        for p in powerups:
            if player.colliderect(p["rect"]):
                active_power = p["type"]
                power_timer = time.time()
                powerups.remove(p)

        # ---------- POWER EFFECTS ----------
        if active_power == "nitro":
            speed = 10
            if time.time() - power_timer > 4:
                active_power = None
                speed = 5

        # ---------- DRAW ----------
        pygame.draw.rect(screen, (0,0,255), player)

        for o in obstacles:
            pygame.draw.rect(screen, (255,0,0), o)

        for p in powerups:
            color = (0,255,0) if p["type"]=="nitro" else (0,0,255)
            pygame.draw.rect(screen, color, p["rect"])

        distance += 1
        coins += 1

        pygame.display.flip()
        clock.tick(60)