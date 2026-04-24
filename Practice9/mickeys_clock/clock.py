import datetime
import pygame


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.center = (self.width // 2, self.height // 2)

        self.original_hand = pygame.image.load("C:/Users/User/Desktop/p2/Practice9/mickeys_clock/images/mickey_hand.png").convert_alpha()

        self.minute_hand = pygame.transform.smoothscale(self.original_hand, (180, 30))
        self.second_hand = pygame.transform.smoothscale(self.original_hand, (140, 24))

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

    def get_angles(self):
        now = datetime.datetime.now()
        minute = now.minute
        second = now.second

        # include seconds so minute hand is accurate
        minute_angle = (minute + second / 60) * 6
        second_angle = second * 6

        return minute, second, minute_angle, second_angle

    def make_rotatable_hand(self, hand_surface):
        """
        Creates a transparent square surface.
        The BASE of the hand is placed at the center of this square.
        Then rotating this square makes the hand behave like a real clock hand.
        """
        size = 400
        canvas = pygame.Surface((size, size), pygame.SRCALPHA)

        hand_rect = hand_surface.get_rect()

        # Put the hand so its LEFT CENTER is exactly in the middle of canvas.
        # This assumes your hand image points to the RIGHT.
        hand_rect.midleft = (size // 2, size // 2)

        canvas.blit(hand_surface, hand_rect)
        return canvas

    def draw_hand(self, hand_surface, angle):
        rotatable = self.make_rotatable_hand(hand_surface)

        # Pygame angle system:
        # 0° points right, but clock 12 o'clock is up.
        rotated = pygame.transform.rotate(rotatable, -angle + 90)

        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def draw_clock_face(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (245, 245, 245), self.center, 170)
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 170, 4)
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 8)

    def draw_time_text(self, minute, second):
        text = self.font.render(f"{minute:02d}:{second:02d}", True, (20, 20, 20))
        rect = text.get_rect(center=(self.center[0], 40))
        self.screen.blit(text, rect)

    def draw(self):
        minute, second, minute_angle, second_angle = self.get_angles()

        self.draw_clock_face()
        self.draw_hand(self.minute_hand, minute_angle)
        self.draw_hand(self.second_hand, second_angle)
        self.draw_time_text(minute, second)