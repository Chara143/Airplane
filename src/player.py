import pygame

from .entity import Entity
from .constants import SHOOT_EVENT1, SHOOT_EVENT2, DISPLAY_SIZE


class Player(Entity):
    def __init__(self, image, coords, speed, health, button):
        super().__init__(image, coords, speed)
        self.health = health
        self.button = button

    def get_damage(self, value):
        self.health -= value

        if self.health <= 0:
            self.kill()
            self.health = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.button:
            left = pressed_keys[pygame.K_a] 
            right = pressed_keys[pygame.K_d]

            if left != right:
                if left:
                    self.move(-self.speed, 0)
                else:
                    self.move(self.speed, 0)

            just_pressed_keys = pygame.key.get_just_pressed()
            if just_pressed_keys[pygame.K_SPACE]:
                pygame.event.post(pygame.Event(SHOOT_EVENT2))
        else:
            left = pressed_keys[pygame.K_LEFT] 
            right = pressed_keys[pygame.K_RIGHT]

            if left != right:
                if left:
                    self.move(-self.speed, 0)
                else:
                    self.move(self.speed, 0)

            just_pressed_keys = pygame.key.get_just_pressed()
            if just_pressed_keys[pygame.K_z]:
                pygame.event.post(pygame.Event(SHOOT_EVENT1))

    def move(self, x, y):
        super().move(x, y)



        if  self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > DISPLAY_SIZE[0]:
            self.rect.right = DISPLAY_SIZE[0]
