from pathlib import Path
import pygame


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 22)

        self.music_dir = Path("music/sample_tracks")
        self.playlist = sorted(
            [file for file in self.music_dir.iterdir() if file.suffix.lower() in [".wav", ".mp3", ".ogg"]]
        )

        self.current_index = 0
        self.is_playing = False

        if self.playlist:
            pygame.mixer.music.load(str(self.playlist[self.current_index]))

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks found"
        return self.playlist[self.current_index].name

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(str(self.playlist[self.current_index]))
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def previous_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def get_position_seconds(self):
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms < 0:
            return 0
        return pos_ms // 1000

    def draw(self, screen):
        screen.fill((240, 240, 240))

        title = self.font.render("Music Player", True, (20, 20, 20))
        screen.blit(title, (20, 20))

        track_text = self.small_font.render(
            f"Track: {self.get_current_track_name()}",
            True,
            (40, 40, 40)
        )
        screen.blit(track_text, (20, 90))

        status = "Playing" if self.is_playing else "Stopped"
        status_text = self.small_font.render(f"Status: {status}", True, (40, 40, 40))
        screen.blit(status_text, (20, 130))

        progress_text = self.small_font.render(
            f"Position: {self.get_position_seconds()} sec",
            True,
            (40, 40, 40)
        )
        screen.blit(progress_text, (20, 170))

        controls = [
            "P = Play",
            "S = Stop",
            "N = Next",
            "B = Previous",
            "Q = Quit"
        ]

        y = 240
        for line in controls:
            text = self.small_font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 35