import pygame
import random
from db import insert_score

class Game:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.snake = [(100, 100)]
        self.direction = (10, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.running = True

    def spawn_food(self):
        return (random.randint(0, 59)*10, random.randint(0, 39)*10)

    def move(self):
        head = (self.snake[0][0] + self.direction[0],
                self.snake[0][1] + self.direction[1])
        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if (head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake[1:]):
            return True
        return False

    def draw(self):
        self.screen.fill((0, 0, 0))

        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, 10, 10))

        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, 10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.direction = (0, -10)
                    if event.key == pygame.K_DOWN:
                        self.direction = (0, 10)
                    if event.key == pygame.K_LEFT:
                        self.direction = (-10, 0)
                    if event.key == pygame.K_RIGHT:
                        self.direction = (10, 0)

            self.move()

            if self.check_collision():
                print("Game Over! Score:", self.score)
                insert_score("Player", self.score)
                self.running = False

            self.draw()
            self.clock.tick(10)

        pygame.quit()