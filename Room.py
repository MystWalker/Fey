#Contains:
#background
#character
#items
#collision (distance formula)
#

import pygame
import pygame.sprite

class Room ( ):
    """Creates a new Room object with passed background and avatar."""
    def __init__ ( self, background, avatar):
        self.background = background #Must be a sprite
        self.avatar = avatar
        self.objects = pygame.sprite.Group()

    def addObject(self, thing):
        """Adds an object to the room's group."""
        self.objects.add(thing)