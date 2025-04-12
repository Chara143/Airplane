import pygame


class Entity():
    def __init__(slef, image, coords, speed):
        slef.image = image.copy()
        slef.rect = slef.image.get_rect(center = coords)
        slef.speed = speed
        slef.mask = pygame.mask.from_surface(image)
        slef.alive = True

    def update(opilki):
        pass

    def render(kraski, win):
        win.blit(kraski.image, kraski.rect)

    def kill(self):
        self.alive = False

    def move(self, x ,y):
        self.rect.move_ip(x, y)

    def collide_entity(self, other):
        return pygame.sprite.collide_mask(self, other)
