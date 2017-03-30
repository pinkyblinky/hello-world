import pygame


class Welcome(object):
    def __init__(self, screen):
        self.screen = screen
        self.status = 'Running'
        self.screen_centerx = screen.get_width()/2
        self.screen_centery = screen.get_height()/2
        print('Welcome is running...')

    def getStatus(self):
        return self.status

    def keydown(self, keyNum):
        print(keyNum)
        # If spacebar is hit, status is 'Done'
        if(keyNum == 32):
            self.status = 'Done'
            
    def setup(self):
        # set the background
        bkgd_color = (255, 255, 255)

        # create the welcom text
        basicfont = pygame.font.SysFont(None, 48)
        msg = 'Welcome to the Math Game!'
        msg += ' Press <space> to begin...'
        col = (255, 0, 0)
        text = basicfont.render(msg, False, col)
        textrect = text.get_rect()
        textrect.centerx = self.screen_centerx
        textrect.centery = self.screen_centery*0.8
  
        # submit everything to the screen
        self.screen.fill(bkgd_color)
        self.screen.blit(text, textrect)
        pygame.display.flip()

