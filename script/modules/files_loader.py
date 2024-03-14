import pygame
from script.modules.pyvidplayer import Video

pygame.init()
pygame.font.init()

def load_image(file, scaleX, scaleY):
    background = pygame.image.load(file)
    background = pygame.transform.scale(background, (scaleX, scaleY))
    return background

def load_video(file, scaleX, scaleY):
    video = Video(file)
    video.set_size((scaleX, scaleY))
    return video

def load_font(font, size):
    font = pygame.font.Font(font, size)
    return font