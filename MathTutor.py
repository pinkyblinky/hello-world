import sys
import pygame
from Welcome import Welcome
from Level1 import Level1
from testMod import testMod

pygame.init()

test = testMod()
test.apple()
print(sys.version)

# build the screen
size = (1500, 1000)
global screen
screen = pygame.display.set_mode(size)
global screen_centerx
screen_centerx = size[0]/2
global screen_centery
screen_centery = size[1]/2

# set the titles
pygame.display.set_caption('Math Tutor')

# initialize the welcome module
currProcess = Welcome(screen)
currProcess.setup()

pygame.display.update()
# set the running logic
currProgress = 0
running = True

while running:
    if currProcess.getStatus() == 'Done':
        currProgress += 1
        if currProgress == 1:
            currProcess = Level1(screen)
            currProcess.setup()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # allows for the 'x' quit
            running = False
        if event.type == pygame.KEYDOWN:
            currProcess.keydown(event.key)

    print('running = ', running)

    
