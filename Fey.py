#Main Runner
#bring in all the views
#add current view to viewmanager

#Starting code ripped from: http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *

#import VeiwManager         #Can't get this to work!!!
#v = VeiwManager([255,255,255], [0,0]) #Puts a white VeiwManager on screen

#Set to True for debug print statements
DEBUG = False

class Fey ( ):
    def __init__ ( self ):
        if(DEBUG):print("Initializing");
        self.RUNNING = True
        self.DISPLAY_SURF = None
        self.SIZE = self.WIDTH, self.HEIGHT = 800, 640
        
    def start ( self ):
        if(DEBUG):print("Starting");
        pygame.init()
        self.DISPLAY_SURF = pygame.display.set_mode(self.SIZE, pygame.DOUBLEBUF)
        self.DISPLAY_SURF.fill((0,0,0))
        pygame.display.flip()
        self.RUNNING = True


    def handleEvent(self, event):
        if(DEBUG):print("Event check");
        if event.type == pygame.QUIT:
            self.RUNNING = False

    def update(self):
        if(DEBUG):print("Updating");
        pass

    def render(self):
        if(DEBUG):print("Rendering");
        #self.DISPLAY_SURF.blit(v.image, v.rect) Dependant on VeiwManager
        pass

    def cleanup(self):
        if(DEBUG):print("Cleaning up");
        pygame.quit()

    def run(self):
        if(DEBUG):print("Attempting to run");
        if self.start() == False:
            self.RUNNING = False

        if(DEBUG):print("Running");
        while(self.RUNNING):
            for event in pygame.event.get():
                self.handleEvent(event)
            self.update()
            self.render()
        self.cleanup()

if __name__ == "__main__":
    runner = Fey ( )
    runner.run ( )
