#Main Runner
#bring in all the views
#add current view to viewmanager

#Starting code ripped from: http://pygametutorials.wikidot.com/tutorials-basic

import pygame
from pygame.locals import *
import pygame.sprite

from ViewManager import ViewManager
from ControlManager import ControlManager
from Character import Character
from Room import Room

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
        #Create display
        self.DISPLAY_SURF = pygame.display.set_mode(self.SIZE)
        self.DISPLAY_SURF.fill((0,0,0))
        #Create Pygame objects here
        self.clock = pygame.time.Clock()
        #Player
        self.player = Character(initial_position = [40,600])
        #Veiw Manager
        self.veiwMan = ViewManager([255,255,255], [5,5], [self.WIDTH-10, self.HEIGHT-10], self.player) #Puts a white VeiwManager on screen
        #Control Manager
        self.conMan = ControlManager()
        self.conMan.setAvatar(self.player)
        #Creating Room
        greenRoom = pygame.sprite.Sprite()
        greenRoom.image = pygame.Surface([1000, 640])
        greenRoom.rect = greenRoom.image.get_rect()
        greenRoom.image.fill([0,255,0])
        self.room1 = Room(greenRoom, self.player) #Sets background to greenRoom and avatar to self.player
        
        pygame.display.flip()
        self.RUNNING = True


    def handleEvent(self, event):
        if(DEBUG):print("Event check");
        if event.type == pygame.QUIT:
            self.RUNNING = False
        #Events are handled here
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            self.veiwMan.setCurrentView(self.room1)
        else:
            self.conMan.handle(event)

    def update(self):
        if(DEBUG):print("Updating");
        #Objects will update themselves (movement, calculation, etc)
        self.player.update()
        pass

    def render(self):
        if(DEBUG):print("Rendering");
        #ViewManager draws apropriate surfaces to itself
        self.veiwMan.drawView()
        self.DISPLAY_SURF.blit(self.veiwMan.image, self.veiwMan.rect) #Dependant on VeiwManager
        pygame.display.flip()
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
            self.clock.tick(30)
            for event in pygame.event.get():
                self.handleEvent(event)
            self.update()
            self.render()
        self.cleanup()

if __name__ == "__main__":
    runner = Fey ( )
    runner.run ( )