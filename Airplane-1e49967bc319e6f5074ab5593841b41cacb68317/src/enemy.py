import pygame
from time import time
from .entity import Entity
from .constants import DISPLAY_SIZE, ENEMY_SHOOT_EVENT


class Enemy(Entity):
    def __init__(self, damage, image, coords, speed):
        super().__init__(image, coords, speed)
        self.damage = damage

    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()

class ShootEnemy(Enemy):
    def __init__(self, damage, image, coords, speed, shoot_interval):
        super().__init__(damage, image, coords, speed)
        self.shoot_interval = shoot_interval
        self.shoot_timer = time()
    def update(self):
        super().update()

        if time() - self.shoot_timer >= self.shoot_interval:
            pygame.event.post(
                pygame.Event(ENEMY_SHOOT_EVENT, coords=self.rect.midbottom, damage=self.damage)
            )
            self.shoot_timer += self.shoot_interval

            
