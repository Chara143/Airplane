import pygame

from src.constants import DISPLAY_SIZE, MAX_FPS, SHOOT_EVENT
from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy


def game(win, clock):
    coords = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    image = pygame.Surface([50, 50])
    image.fill( (255, 0, 0) )
    player = Player(image, coords, 4, 100)

    bullet_image = pygame.Surface([20, 20])
    bullet_image.fill('green')
    bullets = list()

    enemies = list()

    while True:
        #Обраточка собычай
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                b = Bullet(bullet_image, player.rect.midtop,10)
                bullets.append(0)
        
        player.update()
        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        win.fill((0, 0, 0))
        player.render(win)
        for u in bullets:
            u.render(win)
        pygame.display.update()
        clock.tick(MAX_FPS)
        pygame.display.set_caption(str(clock.get_fps()))


def main():
    pygame.init()
    win = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE|pygame.SCALED)
    pygame.display.set_caption("SHOOOOTER")
    clock = pygame.time.Clock()
    while True:
        game(win, clock)


if __name__ == "__main__":
    main()