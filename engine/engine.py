import pygame
import os
import sys
import json

pygame.init()

FPS = 60

rend = pygame.time.Clock()

class Button(pygame.sprite.Sprite):
    def __init__(self, text, textsize: int(), font, textcolor, image):
        global button_text_render
        pygame.sprite.Sprite.__init__(self)
        if image != False  and text == False:
            pygame.image.load(image)
        elif image == False and text != False:
            if textsize != False:
                if textsize == int(textsize):
                    if font != False:
                        button_text = pygame.font.Font(f'src/font/{font}', textsize)
                        button_text_render = button_text.render(text, True, textcolor)
                    else:
                        button_text = pygame.font.Font('src/font/determination.otf', textsize)
                        button_text_render = button_text.render(text, True, textcolor)
                else:
                 TypeError('size can be as integer')
                 #sys.exit()
            else:
                pass
        else:
            pass
    def place(self, xrender, yrender):
        global button_text_render
        window.blit(button_text_render, (W/100*xrender, H/100*yrender))
    

def GetWindow(width, height, name):
    global window
    global W
    global H

    W = width
    H = height 
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption(name)

def ConfigSetting(font):
    global W
    global H

    head_font = pygame.font.Font(f'src/font/{font}', 30)
    head = head_font.render('Screen Format', True, (255,255,255))
    window.blit(head, (W/100*41, H/100 * 20))

    one_ext = Button('1080x720', 20, False, (255,255,255), False)
    one_ext.place(31, 40)

    tue_ext = Button('fullscreen', 20, False, (255,255,255), False)
    tue_ext.place(31, 35)

    thr_ext = Button('400x500', 20, False, (255,255,255), False)
    thr_ext.place(31, 30)

def font(font):
    global base_font
    base_font = font
    return True

def confdata():
    '''проверять существование конфигов игры'''
    if os.path.isdir('data') or os.path.isdir('data/config'):
        if os.path.isfile('data/config/config.json'):
            print('True config file')
        else:
            print('False config file')
            ConfigSetting(font = base_font)
        return True
    else:
        os.mkdir('data')
        os.mkdir('data/config')
        ConfigSetting(font = base_font)
        return 'post-make'
    
def start():
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        
        rend.tick(FPS)
        pygame.display.flip()
        
        
        