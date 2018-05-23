from pygame.locals import *
import pygame

WHITE = (255, 255, 255)
RED = (255,  0,  0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)
pygame.display.flip()

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
 
    def draw(self):
       bx = 0
       by = 0
       for i in range(0, self.M*self.N):
           if self.maze[i] == 1:
               pygame.draw.rect(screen, RED, [bx * 44, by * 44, 50, 20])
               pygame.display.flip()

           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
           
           # this is just meant to be helpful to show what the param
           horizontal_position = 400
           vertical_position = 500
           hieght = 20
           width = 350
           pygame.draw.rect(screen, BLACK, [horizontal_position, vertical_position, width, hieght])
           pygame.display.flip()

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    on_execute = ''
    myMaze = Maze()
    myMaze.draw()

    def __init__(self):
        self.running = True
        self.display_surf = None
        self.image_surf = None
        self.player = Player()

    def on_init(self):
        #pygame.init()
        #self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        
        pygame.display.set_caption('Maze')
        self.running = True
        self.img = pygame.image.load("Pygame.png").convert()
        pygame.display.flip()
 
    def on_event(self, event):
        if event.type == QUIT:
            self.running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        screen.blit(self.img,(self.player.x,self.player.y))
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
