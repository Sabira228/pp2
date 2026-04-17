import datetime
import pygame


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.center = (self.width // 2, self.height // 2)

        self.hand_image = pygame.image.load("images/mickey_hand.png").convert_alpha()

        # Minute hand is a bit longer
        self.minute_hand = pygame.transform.smoothscale(self.hand_image, (180, 30))
        self.second_hand = pygame.transform.smoothscale(self.hand_image, (140, 24))

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

    def get_time_data(self):
        now = datetime.datetime.now()
        minute = now.minute
        second = now.second

        # 360 degrees / 60 units = 6 degrees per minute/second
        # Negative angle = clockwise rotation in pygame.rotate
        minute_angle = -(minute * 6)
        second_angle = -(second * 6)

        return minute, second, minute_angle, second_angle

    def draw_clock_face(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (245, 245, 245), self.center, 170)
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 170, 4)
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 8)

    def draw_hand(self, hand_surface, angle, center_pos):
        rotated = pygame.transform.rotate(hand_surface, angle)
        rect = rotated.get_rect(center=center_pos)
        self.screen.blit(rotated, rect)

    def draw_time_text(self, minute, second):
        text = self.font.render(f"{minute:02d}:{second:02d}", True, (20, 20, 20))
        rect = text.get_rect(center=(self.center[0], 40))
        self.screen.blit(text, rect)

    def draw(self):
        minute, second, minute_angle, second_angle = self.get_time_data()

        self.draw_clock_face()

        # Right hand = minutes
        self.draw_hand(self.minute_hand, minute_angle, self.center)

        # Left hand = seconds
        # Slightly shifted so the two hands are visually different
        self.draw_hand(self.second_hand, second_angle, (self.center[0] - 10, self.center[1] - 10))

        self.draw_time_text(minute, second)