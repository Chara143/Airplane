import pygame

from src.constants import DISPLAY_SIZE, MAX_FPS


def game(win, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        win.fill((0, 0, 0))
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