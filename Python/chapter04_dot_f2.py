#importing stuff i need ::)
import pygame
import pygame.gfxdraw
import random # add our random library
import time

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

running = True

while running:

#def draw a v line
  def draw_vline(screen, a, b, lengtv):
    for i in range(lengtv):
      pygame.gfxdraw.pixel(screen, a, b + i, yellow) 

#def draw a h line (by teacher)
  def draw_hline(screen, x, y, length):
    for i in range(length):
      pygame.gfxdraw.pixel(screen, x + i, y, yellow) 

#trying to draw two lines 
  infoOject = pygame.display.Info()
  x1 = random.randrange(0, infoOject.current_w)
  y1 = random.randrange(0, infoOject.current_h)
  l1 = random.randrange(0,100)
  draw_hline(screen, x1, y1, l1)
  draw_vline(screen, x1, y1, l1)
  draw_hline(screen, x1, y1 + l1 //2, int(l1*0.8))

  pygame.display.flip() # this is how we update the screen we've been drawing on.
  time.sleep(0.03)

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      running = False