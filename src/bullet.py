from .entity import Entity
from .constants import DISPLAY_SIZE


class Bullet1(Entity):
    def update(self):
        self.move(0, -self.speed)
        if self.rect.bottom <= 0:
            self.kill()


class Bullet2(Entity):
    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()
