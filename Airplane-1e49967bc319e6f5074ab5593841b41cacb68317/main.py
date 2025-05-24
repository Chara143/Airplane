from random import randint
import pygame

from src.constants import *
from src.player import Player
from src.bullet import Bullet, EnemyBullet
from src.enemy import Enemy, ShootEnemy
from src.utils import laod_image, get_path


def game(display, clock):
    asteroid_image = laod_image("assets", "images", "asteroid.png", size=[164, 164])
    background_image = laod_image(
        "assets", "images", "background.png", size=DISPLAY_SIZE
    )
    player_image = laod_image("assets", "images", "player.png", size=[96, 96])
    shot_image = laod_image("assets", "images", "shot.png", size=[64, 64])

    coords = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    player = Player(player_image, coords, PLAYER_SPEED, PLAYER_HEALTH)
    shot_sound = pygame.Sound(get_path("assets", "sounds","shot.wav"))
    death_sound = pygame.Sound(get_path("assets", "sounds","death.wav"))
    explosion_sound = pygame.Sound(get_path("assets", "sounds","explosion.wav"))
    

    bullets = list()
    enemies = list()

    difficulty = 0
    score = 0
    font = pygame.Font(get_path("assets","fonts","pixel.ttf"),24)
    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)

    while player.health > 0:
        difficulty += clock.get_time()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == ENEMY_SHOOT_EVENT:
                b = EnemyBullet(
                    pygame.transform.rotate(shot_image, 180),
                    event.coords,
                    BULLET_SPPED,
                )
                bullets.append(b)
            elif event.type == SHOOT_EVENT:
                shot_sound.play()
                b = Bullet(shot_image, player.rect.midtop, BULLET_SPPED)
                bullets.append(b)

            elif event.type == SPAWN_EVENT:
                millis = max(750, round(2000 - difficulty / 70))
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)
                coords = [randint(50, DISPLAY_SIZE[0] - 50), -asteroid_image.height]
                if randint(0, 100) <= 50 - difficulty / 5000:

                    new_image = pygame.transform.rotozoom(asteroid_image, randint(0, 360),1 + randint(-10,+10)/100)

                    e = Enemy(
                        round(ENEMY_DAMAGE + difficulty / 7_000),
                        new_image,
                        coords,
                        ENEMY_SPEED + difficulty / 35_000,
                    )
                    enemies.append(e)

                else:
                    e = ShootEnemy(
                        round(SHOOT_ENEMY_DAMAGE),
                        pygame.transform.rotate(player_image, 180),   
                        coords,
                        SHOOT_ENEMY_SPEED  + difficulty/ 35000,
                        SHOOT_ENEMY_INTERVAL + difficulty/50000 ,
                    )
                    enemies.append(e)
        # Обновление игровых объектов
        player.update()

        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for i in enemies.copy():
            i.update()
            if not i.alive:
                enemies.remove(i)

        for b in bullets:
            if isinstance(b, Bullet):
                for e in enemies:
                    if b.collide_entity(e):
                        explosion_sound.play()
                        b.kill()
                        e.kill()
                        score += 1
            elif b.collide_entity(player):
                player.getdamage(10)
                b.kill()

        for e in enemies:
            if e.collide_entity(player):
                death_sound.play()
                player.get_damage(e.damage)
                e.kill()

        # Обновление экрана
        display.fill("black")
        display.blit(background_image, (0, 0))

        player.render(display)
        for u in bullets:
            u.render(display)
        for u in enemies:
            u.render(display)

        #                             цвет      x   y        ширина      высота
        pygame.draw.rect(display, (100, 0, 0), [10, 10, HEALTH_BAR_WIDTH, 20])
        width = int(player.health / PLAYER_HEALTH * HEALTH_BAR_WIDTH)
        pygame.draw.rect(display, (255, 0, 0), [10, 10, width, 20])
        pygame.draw.rect(display, (175, 0, 0), [8, 8, HEALTH_BAR_WIDTH + 4, 24], 2)

        image_score = font.render(str(score), True, (50, 200, 50))
        rect_score = image_score.get_rect(midtop = [DISPLAY_SIZE[0]/2, 10])
        display.blit(image_score, rect_score)

        pygame.display.update()
        clock.tick(MAX_FPS)


def show_lose(display, clock):
    running = True

    font = pygame.Font(get_path("assets", "fonts", "pixel.ttf"), 64)
    text = font.render("YOU LOSE!", True, (255, 50, 50))
    display.blit(text, text.get_rect(center=[DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]))
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
