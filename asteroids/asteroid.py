import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, *self.containers)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200) , self.position, self.radius, width = 2)
    
    def update(self, dt):
        
        self.position += self.velocity * dt

    def split(self, asteroids):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:  
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroids.add(asteroid1)
            asteroids.add(asteroid2)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
            
