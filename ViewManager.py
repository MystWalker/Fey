#View Manager
#Menu, Game, End of Game
#Contains all views
#Switches in between them.
#add pygame stuff here to be initaliazed

#Some code ripped from: http://www.sacredchao.net/~piman/writing/sprite-tutorial.shtml

import pygame

class ViewManager (pygame.sprite.Sprite):
    def __init__ ( self, color, initial_position ):
        #pygame
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([30,30])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

    def setCurrentView ( self , view ):
        pass

    def drawView ( self , view ):
        pass

