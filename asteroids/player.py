import pygame
from circleshape import *
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)
    
    def rotate(self, dt):
        rotation = PLAYER_TURN_SPEED * dt
        self.rotation += rotation
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
            self.timer = PLAYER_SHOOT_COOLDOWN
            

            
            
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, dt):
        if self.timer <= 0:
            velocity = self.position
            velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, self.radius, velocity)
            
            
        else: 
            return
        
class Shot(CircleShape):

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius, *self.containers)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.position = pygame.Vector2(self.x, self.y)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200) , self.position, self.radius, width = 2)
        
    def update(self, dt):
        self.position += self.velocity * dt