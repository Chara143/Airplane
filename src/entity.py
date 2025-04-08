import pygame


class Entity():
    def __init__(slef, image, coords, speed):
        slef.image = image
        slef.rect = image.get_rect(center = coords)
        slef.speed = speed
        slef.mask = pygame.mask.from_surface(image)

    def update(opilki):
        pass
    def render(kraski, win):
        win.blit(kraski.image,kraski.rect)
