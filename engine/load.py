import pygame
from engine import boot
from engine import engine
import os

global boot_ic


def init():
    '''инцилизация модуля pygame для начала работ'''
    print('WebAn Engine alfa 0.001')
    print('Loading')
    pygame.init()

def music(boot_music):
    '''загрузка музыки из директории src/music/ и сохранение расширения файла музыки'''
    if boot_music == False:
        pass
    elif os.path.isfile(f'src/music/boot/{boot_music}'):
        boot_mus = pygame.mixer.music.load(f'src/music/boot/{boot_music}')
    else:
        pass

def init_win(boot_title, WIDTH, HEIGHT):
    '''инциализация параметров окна'''
    global boot_ic
    
    boot.win(boot_title, boot_ic, WIDTH= WIDTH, HEIGHT = HEIGHT)

def icon(boot_icon):
    '''загрузка иконки окна в последствии указания файла с расширением в src/icon/. 
    Иконка .ico может неправильно загрузиться, поэтому советуем использовать .bmp'''
    global boot_ic
    boot_ic = boot_icon

def run():
    '''обращается к boot целью передать разрешение на загрузку проекта'''
    global boot_ic

    boot.run()

def font(boot_font):
    '''Загрузка шрифта из директории src/font/ и сохранение расширения файла шрифта'''
    pygame.font.init()
    if boot_font == False:
        pass
    elif os.path.isfile(f'src/font/{boot_font}'):
        boot_fn = pygame.font.Font(f'src/font/{boot_font}')
        print(engine.font(font = boot_font))
    else:
        pass
    
    