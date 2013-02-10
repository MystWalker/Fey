#Define character by stats
import pygame
from pygame.locals import *

class Character (pygame.sprite.Sprite):
    def __init__ ( self, color = [255,0,0], initial_position = [0,0], size = [60, 120]):
        #Sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.midbottom = initial_position
        
        #Movement fields
        self.speed = (0,0)
        
        #Symptom intensities
        self.nose = 0
        self.headache = 0
        self.nausea = 0

        #Amount added to symptom every update
        # Idealy these slopes would be controled by separate quadratic
        # equations that would give each symptom a characteristic rhythm
        self.noseSlope = 0.1
        self.headSlope = 0.1
        self.nauseaSlope= 0.1

        #These define the symptom thresholds
        # These may become more complex than single numbers. We may use
        # several thresholds to simulate different stages of suffering.
        self.noseThresh = 1
        self.headThresh = 0.5
        self.nauseaTresh= 1
    

    def sneeze(self):
        print("Achoo!")#Game relivant code here


    def pound(self):
        print("Argh!")#Game relivant code here


    def vomit(self):
        print("Hurgle!")#Game relivant code here
        
    def move(self, event):
        if event.type == pygame.KEYDOWN and event.key == K_LEFT:
            self.speed = (-10,0)
        elif event.type == pygame.KEYUP and event.key == K_LEFT:
            self.speed = (0,0)
        elif event.type == pygame.KEYDOWN and event.key == K_RIGHT:
            self.speed = (10,0)
        elif event.type == pygame.KEYUP and event.key == K_RIGHT:
            self.speed = (0,0)

    def update(self):
        #Movement
        x, y = self.rect.midbottom
        
        self.rect.move_ip(self.speed)
        
        """ #Deactivated for now
        
        #Illness
        self.nose = self.nose + self.noseSlope
        self.headache = self.headache + self.noseSlope
        self.nausea = self.nausea + self.nauseaSlope

        #These check the different symptom thresholds
        if(self.nose >= self.noseThresh):
            self.sneeze()

        if(self.headache >= self.headThresh):
            self.pound()

        if(self.nausea >= self.nauseaTresh):
            self.vomit()
            
        #"""


#Test Main
if __name__ == '__main__':

    john = Character()

    while(john.nausea < 1):
        print("Nose: " + str(john.nose))
        print("Headache: " + str(john.headache))
        print("Nausea: " + str(john.nausea) + "\n")
        john.update()

    print("Oh, this terible cold...\n")
    john.noseSlope = john.noseSlope * -1
    john.headSlope = john.headSlope * -1
    john.nauseaSlope = john.nauseaSlope * -1

    while(john.nausea > 0.0):
        print("Nose: " + str(john.nose))
        print("Headache: " + str(john.headache))
        print("Nausea: " + str(john.nausea) + "\n")
        john.update()

    print("Ah, much better.")