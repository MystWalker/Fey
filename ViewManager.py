#View Manager
#Menu, Game, End of Game
#Contains all views
#Switches in between them.
#add pygame stuff here to be initaliazed

#Some code ripped from: http://www.sacredchao.net/~piman/writing/sprite-tutorial.shtml

import pygame
from pygame.sprite import Group #Used for sprite organization
from Character import Character
from CollisionManager import CollisionManager

DEBUG = False

class ViewManager (pygame.sprite.Sprite):
    def __init__ ( self, color, initial_position, size, player = None ):
        """Creates a new ViewManager object."""
        #Sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

        #Drawable objects
        if (player == None):
            self.player = Character()
        else: self.player = player

        #Draw starting objects
        #self.setup()

        #Sprite Groups
        self.activeObjects = Group()
        self.activeBackground = Group()
        self.activeAvatar = pygame.sprite.GroupSingle()
        
        #Collision
        self.collision = CollisionManager()

    def setup(self):
        """Does nothing at this point."""
        #self.image.blit(self.player.image, self.player.rect) #Draw player onto self
        pass

    def update(self):
        """Calls the update method of all active objects, checks for colisions with player."""
        self.collision.update()
        
        self.activeObjects.update()
        self.activeBackground.update()
        self.activeAvatar.update()
        

    def setCurrentView ( self , view ):
        """Replaces current active objects with those of the passed view."""
        if(DEBUG):print("Setting view");
        self.activeBackground.empty() #Get rid of old background
        self.activeObjects.empty() #Get rid of old objects
        self.activeAvatar.empty() #Get rid of old Avatar

        #Adds new background, objects, and avatar
        self.activeBackground.add(view.background)
        self.activeObjects.add(view.objects)
        self.activeAvatar.add(view.avatar)
        
        #Passes CollisionManager active objects
        self.collision.setActiveObjects(self.activeObjects, self.activeAvatar)
        
        
        pass

    def drawView ( self ):
        """Draws sprites in the proper order for depth
        
        1. Background
        2. Objects
        3. Player avatar
        
        """
        self.activeBackground.draw(self.image)
        self.activeObjects.draw(self.image)
        self.activeAvatar.draw(self.image)
        pass

