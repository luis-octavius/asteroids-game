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

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Infinite loop to keep the game up and running
    while True:
        # Quit game in X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
        screen.fill("black") # Background
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # FPS

if __name__ == "__main__":
    main()
