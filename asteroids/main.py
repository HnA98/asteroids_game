import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    split_asteroids = pygame.sprite.Group()


    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, split_asteroids, updatables, drawables)
    AsteroidField.containers = (updatables, )
    Shot.containers = (shots, updatables, drawables)
    asteroid_field = AsteroidField()
    
    
    player1 = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                pygame.quit()
        screen.fill("black")

        updatables.update(dt)

        for asteroid in asteroids:

            for shot in shots:
                if asteroid.check_collision(shot) == True:
                    asteroid.split(asteroids)
                    asteroids.update(dt)
                    shot.kill()

            if asteroid.check_collision(player1) == True:
                print("GAME OVER!")
                return 0
            
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
