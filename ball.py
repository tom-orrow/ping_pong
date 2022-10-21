import pygame
import random

from settings import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, game, groups):
        super().__init__(groups)
        self.game = game
        self.radius = 8
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.pos = pygame.math.Vector2(self.game.screen_rect.center)
        self.rect = self.image.get_rect(center=self.pos)

        pygame.draw.circle(
            self.image,
            "white",
            center=(self.radius, self.radius),
            radius=self.radius,
        )

        # start with random direction
        self.default_speed = 300
        self.speed = self.default_speed
        self.direction = pygame.math.Vector2(self.speed, 0).rotate(
            self.get_random_angle()
        )

    def update(self):
        self.collision()
        print(self.speed)
        self.speed = self.default_speed + pygame.time.get_ticks() // 100

        # move
        self.pos += self.direction * self.game.dt
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def reset(self):
        self.pos = pygame.math.Vector2(self.game.screen_rect.center)
        self.rect = self.image.get_rect(center=self.pos)
        self.direction = pygame.math.Vector2(self.speed, 0).rotate(
            self.get_random_angle()
        )

    def collision(self):
        # wall bounce
        if self.pos.y <= 0 or self.pos.y >= HEIGHT:
            self.direction.y = -self.direction.y

        # out of boundaries
        if self.rect.left < 0:
            self.game.score.player2_score += 1
            self.reset()
        elif self.rect.right > self.game.screen_rect.right:
            self.game.score.player1_score += 1
            self.reset()

        # player bounce
        collision = pygame.sprite.spritecollide(self, self.game.player_group, False)
        if collision:
            player = collision[0]
            relative = (self.rect.midleft[1] - player.rect.centery) / (
                player.rect.height / 2
            )
            if player.rect.x < 100:
                # player 1
                self.direction = pygame.math.Vector2(self.speed, 0).rotate(
                    75 * relative
                )
            else:
                # player 2
                self.direction = pygame.math.Vector2(-self.speed, 0).rotate(
                    -75 * relative
                )

    def get_random_angle(self):
        while True:
            angle = random.randrange(360)
            if 30 < abs(angle) or 180 - abs(angle) < 30:
                return angle

        return angle
