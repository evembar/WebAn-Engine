import pygame
from engine import engine
from engine.engine import *


engine.GetWindow(width=1080, height=560, name = 'WebAn Engine')

example = Button('пример', 20, False, (255,255,255), False)
example.place(31, 50)

#engine.confdata()
engine.start()