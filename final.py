from pygame.locals import *
import pygame

class Player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed
        
    def moveLeft(self):
        self.x = self.x - self.speed
        
    def moveUp(self):
        self.y = self.y - self.speed
        
    def moveDown(self):
        self.y = self.y + self.speed

class Maze:
    def __init__(self):
       self.M = 10
       self.N = 10
       self.maze = [ 0,0,0,0,0,0,0,0,0,0,
                     0,1,0,1,1,1,1,0,1,1,
                     0,0,1,1,1,1,0,1,1,1,
                     1,1,1,0,0,1,1,1,0,0,
                     1,0,1,1,1,0,0,1,1,1,
                     1,0,0,0,1,1,1,1,0,0,
                     1,1,1,1,0,0,0,0,0,0,
                     0,0,0,1,1,1,1,1,1,0,
                     1,1,1,0,0,0,0,0,1,0,
                     1,0,1,1,1,1,1,1,1,0,]
 
    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           print(i)
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))
 
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
 
class App:

    windowWidth = 800
    windowHight = 600
    player = 0
    on_execute = ''

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Maze')
        self.running = True
        self.image_surf = pygame.image.load("Pygame.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self.running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self.display_surf.fill((0,0,0))
        self.display_surf.blit(self.image_surf,(self.player.x,self.player.y))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while (self.running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            elif(keys[K_LEFT]):
                self.player.moveLeft()

            elif(keys[K_UP]):
                self.player.moveUp()

            elif(keys[K_DOWN]):
                self.player.moveDown()

            elif(keys[K_ESCAPE]):
                self.running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    App = App()
    App.on_execute()
