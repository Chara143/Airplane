from random import randint
import pygame

from src.constants import (
    MAX_FPS,
    DISPLAY_SIZE,
    SHOOT_EVENT1,
    SHOOT_EVENT2,
    PLAYER_HEALTH,
    PLAYER_SPEED,
    BULLET_SPPED,
)
from src.player import Player
from src.bullet import Bullet1, Bullet2
from src.utils import laod_image, get_path


def game(display, clock):
    background_image = laod_image(
        "assets", "images", "background.png", size=DISPLAY_SIZE
    )
    player1_image = laod_image("assets", "images", "player.png", size=[96, 96])
    player2_image = pygame.transform.rotate(laod_image("assets", "images", "player.png", size=[96, 96]), 180)
    shot_image1 = laod_image("assets", "images", "shot.png", size=[64, 64])
    shot_image2 = pygame.transform.rotate(laod_image("assets", "images", "shot.png", size=[64, 64]), 180)

    coords_1 = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    coords_2 = DISPLAY_SIZE[0] / 2, 50
    player_1 = Player(player1_image, coords_1, PLAYER_SPEED, PLAYER_HEALTH, True)
    player_2 = Player(player2_image, coords_2, PLAYER_SPEED, PLAYER_HEALTH, False)
    shot_sound = pygame.Sound(get_path("assets", "sounds","shot.wav"))
    death_sound = pygame.Sound(get_path("assets", "sounds","death.wav"))
    explosion_sound = pygame.Sound(get_path("assets", "sounds","explosion.wav"))
    

    bullets = list()
    font = pygame.Font(get_path("assets","fonts","pixel.ttf"),24)

    while player_1.health > 0:

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == SHOOT_EVENT1:
                shot_sound.play()
                b = Bullet1(shot_image1, player_1.rect.midtop, BULLET_SPPED)
                bullets.append(b)
            elif event.type == SHOOT_EVENT2:
                shot_sound.play()
                b = Bullet2(shot_image2, player_2.rect.midbottom, BULLET_SPPED)
                bullets.append(b)


        # Обновление игровых объектов
        player_1.update()
        player_2.update()

        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for b in bullets:
            if isinstance(b, Bullet1) and b.collide_entity(player_2):
                explosion_sound.play()
                b.kill()
                player_2.get_damage(10)
            if isinstance(b, Bullet2) and b.collide_entity(player_1):
                explosion_sound.play()
                b.kill()
                player_1.get_damage(10)


        # Обновление экрана
        display.fill("black")
        display.blit(background_image, (0, 0))

        player_1.render(display)
        player_2.render(display)
        for u in bullets:
            u.render(display)

        xy = player_1.rect.midtop
        width = player_1.rect.width
        pramoygolnik = pygame.Rect(xy[0] - width/2, xy[1] - 10, width, 10)
        pramoygolnik2 = pygame.Rect(xy[0] - width/2, xy[1] - 10, int(width * player_1.health / PLAYER_HEALTH), 10)
        pygame.draw.rect(display, (1, 1, 1), pramoygolnik)
        pygame.draw.rect(display, (50, 255, 50), pramoygolnik2)

        xy = player_2.rect.midbottom
        width = player_2.rect.width
        pramoygolnik = pygame.Rect(xy[0] - width/2, xy[1] - 10, width, 10)
        pramoygolnik2 = pygame.Rect(xy[0] - width/2, xy[1] - 10, int(width * player_2.health / PLAYER_HEALTH), 10)
        pygame.draw.rect(display, (1, 1, 1), pramoygolnik)
        pygame.draw.rect(display, (255, 50, 50), pramoygolnik2)

        pygame.display.update()
        clock.tick(MAX_FPS)


def show_lose(display, clock):
    running = True

    font = pygame.Font(get_path("assets", "fonts", "pixel.ttf"), 64)
    text = font.render("PLAYER 2 WON!", True, (255, 50, 50))
    display.blit(text, text.get_rect(center=[DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]))
    pygame.display.update()


    font1 = pygame.Font(get_path("assets", "fonts", "pixel.ttf"), 64)
    text1 = font1.render("PLAYER 1 WON!", True, (50, 255, 50))
    display.blit(text1, text1.get_rect(center=[DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False

        clock.tick(MAX_FPS)


def main():
    pygame.init()

    display = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption("Shooter")
    clock = pygame.time.Clock()

    pygame.mixer.music.load(get_path("assets", "music", "background-1.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while True:
        game(display, clock)
        show_lose(display, clock)


if __name__ == "__main__":
    main()
