import pygame

from random import randint
from src.constants import DISPLAY_SIZE, MAX_FPS, SHOOT_EVENT, SPAWN_EVENT
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

    enemy_image = pygame.Surface([50, 50])
    enemy_image.fill('white')
    enemies = list()

    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)
    difficulty = 0 


    while True:
        difficulty += clock.get_time()


        #Обраточка собычай
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                b = Bullet(bullet_image, player.rect.midtop,10)
                bullets.append(0)
            elif event.type == SPAWN_EVENT:
                millies = round(2000- difficulty/70)
                pygame.time.set_timer(SPAWN_EVENT, millies, 1)

                e = Enemy(enemy_image, [randint(50, DISPLAY_SIZE[0] - 50), - enemy_image.height], 5 + difficulty/35_000, round(10 + difficulty/7000))
                enemies.append(e)
        
        player.update()
        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for i in enemies.copy():
            i.update()
            if not i.alive:
                enemies.remove(i)

        win.fill((0, 0, 0))
        player.render(win)
        for u in bullets:
            u.render(win)
        for u in enemies:
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