import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, player_num, groups):
        super().__init__(groups)
        self.game = game

        self.player_num = player_num
        self.image = pygame.Surface((10, PLAYER_HEIGHT))
        self.image.fill("white")
        self.speed = 1000

        if self.player_num == 1:
            self.pos = pygame.math.Vector2(
                0, self.game.screen_rect.midleft[1] - (PLAYER_HEIGHT / 2)
            )
        else:
            self.pos = pygame.math.Vector2(
                self.game.screen_rect.width - 10,
                self.game.screen_rect.midright[1] - (PLAYER_HEIGHT / 2),
            )

        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        # events
        pressed_keys = pygame.key.get_pressed()
        if self.player_num == 1:
            button_up, button_down = pygame.K_w, pygame.K_d
        else:
            button_up, button_down = pygame.K_p, pygame.K_l

        if pressed_keys[button_up]:
            if self.rect.top > 0:
                self.pos.y -= self.speed * self.game.dt
        elif pressed_keys[button_down]:
            if self.rect.bottom < self.game.screen_rect.bottom:
                self.pos.y += self.speed * self.game.dt

        # move
        self.rect.topleft = round(self.pos.x), round(self.pos.y)
