#View Manager
#Menu, Game, End of Game
#Contains all views
#Switches in between them.
#add pygame stuff here to be initaliazed

#Some code ripped from: http://www.sacredchao.net/~piman/writing/sprite-tutorial.shtml

import pygame
from pygame.sprite import Group #Used for sprite organization
from Character import Character

class ViewManager (pygame.sprite.Sprite):
    def __init__ ( self, color, initial_position, size, player = None ):
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
        self.setup()

        #Sprite Groups
        self.activeObjects = Group()
        self.activeBackground = Group()

    def setup(self):
        self.image.blit(self.player.image, self.player.rect) #Draw player onto self
        pass

    def update(self):
        pass

    def setCurrentView ( self , view ):
        self.activeBackground.empty() #Get rid of old background
        self.activeObjects.empty() #Get rid of old objects

        #Adds new background and objects
        self.activeBackground.add(view.background)
        self.activeObjects.add(view.objects) 
        pass

    def drawView ( self ):
        self.activeBackground.draw(self.image)
        self.activeObjects.draw(self.image)
        pass

