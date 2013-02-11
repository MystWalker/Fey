#ControlManager

#This modual handles all input and makes sure that the proper
#objects are awear of the events that are relevant to them

import pygame
from pygame.locals import *

DEBUG = False

class ControlManager():
    def __init__(self):
        """Creates a new ControlManager object."""
        self.currentAvatar = pygame.sprite.GroupSingle()
        self.lastAvatar = pygame.sprite.GroupSingle()

    def setAvatar(self, newAvatar):
        """Sets the passed avatar to be the new current."""
        self.lastAvatar.add(self.currentAvatar)
        self.currentAvatar.add(newAvatar)

    def handle(self, event):
        """Passes event to current avatar's move() function."""
        if(DEBUG):print("Handling: " + str(event.type));
        self.currentAvatar.sprite.move(event)
        pass

if __name__ == "__main__":
    control = ControlManager()
