import pygame

from settings import *


class Score:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("assets/subatomic.ttf", 50)
        self.player1_score = 0
        self.player2_score = 0
        self.color = (50, 50, 50)
        self.score_text = None
        self.image = None
        self.rect = None

    def update(self):
        self.score_text = f"{self.player1_score} : {self.player2_score}"
        self.image = self.font.render(self.score_text, True, self.color)
        self.rect = self.image.get_rect(midbottom=(WIDTH / 2, HEIGHT - 80))

        self.game.screen.blit(self.image, self.rect)
        pygame.draw.rect(
            self.game.screen,
            self.color,
            self.rect.inflate(60, 60),
            width=8,
            border_radius=5,
        )
