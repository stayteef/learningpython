import pygame
import pygame.gfxdraw
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
myfont = pygame.font.SysFont('Comic Sans MS', 30)

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
   
# Add a new list before our loop starts, otherwise, the list gets forgotten every time the loop completes
cursorList = []
eraserList = []
#colorList = []
size1 = 6
color = white

while running:
    textsurface = myfont.render('arrow keys for direction\n hold Space to draw\nhold Delete to erase\n1-5 for stroke size', False, white)
    #starting screen setup
    screen.fill(black)
    draw_plus_sign(screen, plusX, plusY, 15, white)
    key = pygame.key.get_pressed()
    screen.blit(textsurface,(0,0))

    # loop over each of our cursor positions. if empty, skips iteration
    for plusSign in cursorList:
       #colorandom = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        draw_plus_sign(screen, plusSign[0], plusSign[1], plusSign[2], plusSign[3])
        
        #setting up stroke size
        if key[pygame.K_1]:
            size1 = 8
        if key[pygame.K_2]:
            size1 = 10
        if key[pygame.K_3]:
            size1 = 13
        if key[pygame.K_4]:
            size1 = 16
        if key[pygame.K_5]:
            size1 = 20
        #setting color
        if key[pygame.K_r]:
            color = (255,0,0)
        if key[pygame.K_b]:
            color = (0,0,255)
        if key[pygame.K_g]:
            color = (0,128,0)
        if key[pygame.K_y]:
            color = (255,255,0)
        if key[pygame.K_w]:
            color = white
        if key[pygame.K_x]:
            color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    # add new check for the SPACEBAR
    if key[pygame.K_SPACE]:
        # take the current position of the cursor and create a list holding x and y
        newPlace = [plusX, plusY, size1, color]
        # add that list to our cursorList
        cursorList.append(newPlace)
        #colorList.append(colorandom)
        #color = colorList[-1]       

    #ERASER (by drawing black)
    for plusSign in eraserList:
      draw_plus_sign(screen, plusSign[0], plusSign[1], plusSign[2], black)
    if key[pygame.K_BACKSPACE] or key[pygame.K_DELETE]:
        erase = [plusX, plusY, size1]
        eraserList.append(erase)

    if key[pygame.K_UP]:
        plusY = plusY - 2
    elif key[pygame.K_DOWN]:
        plusY = plusY + 2
    if key[pygame.K_LEFT]:
        plusX = plusX - 2
    elif key[pygame.K_RIGHT]:
        plusX = plusX + 2

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        running = False

    pygame.display.flip() # this is how we update the screen we've been drawing on.
    clock.tick(90) 