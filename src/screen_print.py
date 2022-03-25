__author__ = 'srkiyengar'


import pygame


#Acknowledgement - code modified from http://www.pygame.org/docs/ sample


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = (255, 0, 0)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information on a screen (pygame.display)


class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def Screenprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

    def Yspace(self):
        self.y += 10


class CounterPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 100)

    def Screenprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, RED)
        screen.blit(textBitmap, [self.x, self.y])

    def reset(self):
        self.x = 10
        self.y = 350
        self.line_height = 65

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

    def Yspace(self):
        self.y += 100

