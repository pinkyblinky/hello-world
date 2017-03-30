import pygame


class Level1(object):
    def __init__(self, screen):
        self.screen = screen
        self.status = 'Running'
        self.screen_centerx = screen.get_width()/2
        self.screen_centery = screen.get_height()/2
        print('Level 1 is running...')

    def getStatus(self):
        return self.status

    def keydown(self, keyNum):
        print(keyNum)

    def setup(self):

        # set the background
        bkgd_color = (230, 230, 255)

        # create the grass
        grass_color = (0, 100, 0)
        grass_marker = (0, self.screen_centery*1.75)
        tmp_width = self.screen.get_width()
        tmp_height = self.screen.get_height()
        grass = pygame.Surface((tmp_width, tmp_height),)
        rec_args = (0, 0, tmp_width, tmp_height)
        args = (grass, grass_color, rec_args, 0)
        pygame.draw.rect(*args)

        # construct the knight
        knight_img = pygame.image.load('Knight.png')
        tmp_width = knight_img.get_width()
        tmp_height = knight_img.get_height()
        dims = (tmp_width, tmp_height)
        args = (dims, pygame.SRCALPHA, 32)
        knight = pygame.Surface(*args)
        knight = knight.convert_alpha()
        knight.blit(knight_img, (0, 0))
        knight = pygame.transform.flip(knight, 1, 0)
        tmp_xmark = self.screen_centerx*0.05
        knight_marker = (tmp_xmark, grass_marker[1]-tmp_height)

        # submit everything to the screen
        self.screen.fill(bkgd_color)
        self.screen.blit(grass, grass_marker)
        self.screen.blit(knight, knight_marker)
        pygame.display.flip()
