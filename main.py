import pygame
from constants import *
from player import Player
from asteroid import Asteroid 
from asteroidfield import AsteroidField

def main():
    print(f"""
        Starting Asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
    """)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Groups allow us to create lists. In the containers of the classes, we can add these lists that puts all of the objects created from this class in the categories containerized
    # Now we can use methods like 'update' only a single time to update all sprites. Or we can iterate through one of these groups and call a method 

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    # Infinite loop to keep the game up and running
    while True:
        # Quit game in X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return 
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.get_collision(player):
                print("Game Over!")
                pygame.QUIT()

        screen.fill("black")

        for thing in drawables:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # FPS limit to 60 - miliseconds to seconds

if __name__ == "__main__":
    main()
