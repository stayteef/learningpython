import pygame

#pygame.gfxdraw is a pygame module for drawing shapes
import pygame.gfxdraw

#make sure python gets set up
pygame.init()

#set height and width of screen
screenWidth = 800
screenHeight = 800

#create a screen
#pygame.display is a module to control the display window and screen; and set_mode is a function under this module to nitialize a window or screen for display
screen = pygame.display.set_mode((screenWidth, screenHeight))

white = (255,255,255)
black = (0,0,0)

#setting a variable called 'running'
running = True

#while loop
while running:

    screen.fill(black)


    # surface (Surface) -- surface to draw on
    # x (int) -- x coordinate of the pixel
    # y (int) -- y coordinate of the pixel
    # color (Color or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])

    for i in range(266, 532):
      pygame.gfxdraw.pixel(screen, i, screenHeight // 2, white) 
    for i in range(266, 532):
      pygame.gfxdraw.pixel(screen, i, 266, white) 
    for h in range(266, 532):
      pygame.gfxdraw.pixel(screen, 266, h, white) 


#event.get is a function to get events from the queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#pygame.display.flip is to update the full display Surface to the screen
    pygame.display.flip() 