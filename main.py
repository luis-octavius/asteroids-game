import pygame
from constants import *
from player import Player

def main():
    print(f"""
        Starting Asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
    """)

    pygame.init()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Drawables: ", drawables)
    # Infinite loop to keep the game up and running
    while True:
        # Quit game in X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
        updatables.update(dt)

        screen.fill("black")

        for thing in drawables:
            thing.draw(screen)

        dt = clock.tick(60) / 1000 # FPS limit to 60 - miliseconds to seconds

        pygame.display.flip()
        # print("DT: ", dt)

if __name__ == "__main__":
    main()
