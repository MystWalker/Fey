#Contains:
#background
#character
#items
#collision (distance formula)
#

import pygame
import pygame.sprite

class Room ( ):
    def __init__ ( self, background, avatar):
        self.background = background #Must be a sprite
        self.avatar = avatar
        self.objects = pygame.sprite.Group()
        pass

    #adds an object to the room's group
    def addObject(self, thing):
        self.objects.add(thing)

