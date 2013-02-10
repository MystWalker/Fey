#Item class
#id
#name
#dialog
#use dialog
#position
#state
# 0 - not picked up
# 1 - picked up
# 2 - used

import pygame
from pygame.locals import *

DEBUG = False

class Item (pygame.sprite.Sprite):
    def __init__ (self, initial_position = [25,50]):
        #Sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([50,50])
        self.image.fill([0,0,255])

        self.rect = self.image.get_rect()
        self.rect.midbottom = initial_position
        
        self.touched_event = pygame.event.Event(NOEVENT)
        
        self.TOUCHED = False
        
    def update(self):
        if(DEBUG):print("Updating");
        if(not self.TOUCHED): self.image.fill([0,0,255])
        
    def touched(self):
        if(DEBUG): print("Touched");
        self.image.fill([0,100,100])
        if(DEBUG): print("Posting: " + str(self.touched_event))
        pygame.event.post(self.touched_event)
        
    def setTouchEvent(self, event):
        self.touched_event = event
        
#Test Main
if __name__ == '__main__':
    DISPLAY_SURF = pygame.display.set_mode([300,300])
    DISPLAY_SURF.fill((0,0,0))
    
    box = Item()
    
    go = True
    
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
        DISPLAY_SURF.blit(box.image, box.rect)
        pygame.display.flip()
    pygame.quit()