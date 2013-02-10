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
from Item import Item

#Set to True for debug print statements
DEBUG = False

class Fey ( ):
    def __init__ ( self ):
        """Sets game instance fields and sets RUNNING to True. No return."""
        
        if(DEBUG):print("Initializing");
        self.RUNNING = True
        self.DISPLAY_SURF = None
        self.SIZE = self.WIDTH, self.HEIGHT = 800, 640
        
    def start ( self ):
        """Creates all game object instances. No return.
        
        This is where specific Rooms, Items, Cotrollers, and pygame essentials are
        created.
        
        """
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
        #Creating Rooms
        greenRoom = pygame.sprite.Sprite()
        greenRoom.image = pygame.Surface([1000, 640])
        greenRoom.rect = greenRoom.image.get_rect()
        greenRoom.image.fill([0,255,0])
        self.room1 = Room(greenRoom, self.player) #Sets background to greenRoom and avatar to self.player
        
        grayRoom = pygame.sprite.Sprite()
        grayRoom.image = pygame.Surface([1000, 640])
        grayRoom.rect = grayRoom.image.get_rect()
        grayRoom.image.fill([100,100,100])
        self.room2 = Room(grayRoom, self.player)
        
        #Creating items
        self.box = Item([400, 600])
        self.box.setTouchEvent(pygame.event.Event(25, {"room":self.room2}))
        self.box2 = Item([200, 600])
        self.box2.setTouchEvent(pygame.event.Event(25, {"room":self.room1}))
        self.room1.addObject(self.box)
        self.room2.addObject(self.box2)
        self.itemGroup = pygame.sprite.RenderPlain(self.box,self.box2)
        
        #Making Text
        #This is not critical code
        if(pygame.font.get_init):
            hello = pygame.font.Font(None,64)
            hello = hello.render("Press Space", False, [0,0,0])
            x,y = self.veiwMan.rect.center
            x = x - (hello.get_width()/2)
            y = y - (hello.get_height()/2)
            self.veiwMan.image.blit(hello, [x,y])
        
        pygame.display.flip()
        self.RUNNING = True


    def handleEvent(self, event):
        """Pipes given event to relivant reciver. No return.
        
        This method handles event calls and sorts them either to the main game instance,
        to the game's ControlManager, or the game's VeiwManager. It may be better to put
        this functionality into a standalone class.
        
        """
        if(DEBUG):print("Event check");
        if event.type == pygame.QUIT:
            self.RUNNING = False
        #Events are handled here
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            self.RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            callChange = pygame.event.Event(25, {"room":self.room1})
            pygame.event.post(callChange)
        elif event.type == pygame.KEYDOWN and event.key == K_DOWN:
            callChange = pygame.event.Event(25, {"room":self.room2})
            pygame.event.post(callChange)
        elif(event.type == 25): #Event #25 is a changeRoom call
            self.veiwMan.setCurrentView(event.room)
        else:
            self.conMan.handle(event)

    def update(self):
        """Main update function. Should be called every cicle. No return.
        
        This function calls the update functions of all active game objects.
        
        """
        if(DEBUG):print("Updating");
        #Objects will update themselves (movement, calculation, etc)
        self.veiwMan.update()

    def render(self):
        """Draws the final frame onto the display. No return.
        
        This function calls the ViewManager to blit (draw) all active objects 
        to itself, then blits itself onto the main display, and then calls the
        display to flip the changes to the screen.
        
        """
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