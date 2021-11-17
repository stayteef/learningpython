import pygame
import pygame.gfxdraw

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
 
running = True

#def draw a h line 
def draw_hline(screen, x1, y1, length, color):
    for x in range(x1, x1 + length):
        pygame.gfxdraw.pixel(screen, x, y1, color)

#def draw a v line 
def draw_vline(screen, x1, y1, length, color):
    for y in range(y1, y1 + length):
        pygame.gfxdraw.pixel(screen, x1, y, color)

#using the code above to draw a plus sign
def draw_plus_sign(screen, x, y, size, color):
        draw_hline(screen, x - (size // 2), y, size, color)
        draw_vline(screen, x, y - (size // 2), size, color)

w, h = pygame.display.get_surface().get_size()

# set the start points to the center of the screen
plusX = w // 2
plusY = h // 2
   
while running:
    screen.fill(black)
    
    # every loop, draw the plus sign again at new position
    draw_plus_sign(screen, plusX, plusY, 15, white)

    #ADDING KEY PRESS!!!!!!
    # get the list of keys that are pressed / not pressed
    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP]:
        plusY = plusY - 10
    elif key[pygame.K_DOWN]:
        plusY = plusY + 10
    if key[pygame.K_LEFT]:
        plusX = plusX - 10
    elif key[pygame.K_RIGHT]:
        plusX = plusX + 10

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        running = False
    pygame.display.flip() # this is how we update the screen we've been drawing on.
    clock.tick(90) 