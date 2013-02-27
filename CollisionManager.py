#CollisionManager
#Handles the logic for coliding active objects

import pygame
from pygame.locals import *
from pygame.sprite import Group #Used for sprite organization
from pygame.sprite import GroupSingle

DEBUG = False

class CollisionManager():
    def __init__(self):
        """Initializes CollisionManager with organizing sprite Groups."""
        self.activeObjects = Group()
        self.activeAvatar = GroupSingle()
        
        
    def setActiveObjects(self, activeObjects, activeAvatar):
        """Sets active objects to that of passed sprite Groups."""
        #self.activeObjects.empty()
        self.activeObjects = activeObjects
        
        #if(activeAvatar != None):
        self.activeAvatar = activeAvatar
        #else:
        #    self.activeAvatar.empty()
            
        if(DEBUG):print("Active objects set.");
        
    def update(self):
        """Checks for collision of groups and takes appropriate action."""
        
        #Player collisions
        if(self.activeAvatar):
            collisions = pygame.sprite.spritecollide(self.activeAvatar.sprite, self.activeObjects, False)
            if(collisions):
                for item in collisions:
                    item.touched()
                    self.activeAvatar.sprite.collisions.add(item)
