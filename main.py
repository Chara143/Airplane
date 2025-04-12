import pygame

from src.constants import DISPLAY_SIZE, MAX_FPS, SHOOT_EVENT
from src.player import Player


def game(win, clock):
    coords = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    image = pygame.Surface([50, 50])
    image.fill( (255, 0, 0) )
    player = Player(image, coords, 4, 100)
    while True:
        #Обраточка собычай
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                print(1)
        
        player.update()

        win.fill((0, 0, 0))
        player.render(win)
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