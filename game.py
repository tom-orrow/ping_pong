import sys
import pygame

from settings import *
from player import Player
from ball import Ball
from score import Score


class Game:
    def __init__(self):
        # base
        pygame.init()
        pygame.display.set_caption("Pingy Pongy")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.all_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player1 = Player(self, 1, [self.all_group, self.player_group])
        self.player2 = Player(self, 2, [self.all_group, self.player_group])
        self.ball = None
        self.score = Score(self)

    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                    and self.ball is None
                ):
                    self.ball = Ball(self, [self.all_group])

            # frame rate limit
            self.dt = self.clock.tick(120) / 1000

            # update
            self.screen.fill("black")
            self.all_group.update()

            # drawing
            self.score.update()
            self.all_group.draw(self.screen)

            # final frame
            pygame.display.update()


if __name__ == "__main__":
    Game().run()
