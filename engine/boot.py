import pygame
import sys
import os
import random
from engine import engine
from moviepy.editor import VideoFileClip
from engine.pyvidplayer import Video
import time

global W
global H
boot_active = False

confdatad = False
clock = pygame.time.Clock()
FPS = 60
EnableAnimate = 0
EnableEffect = 0
particles = []

class animate_logo(pygame.sprite.Sprite):
    '''сборка логотипа в виде спрайта '''
    def __init__(self, WS, boot_image, type):
        global boot_im
        global boot_im_rc

        pygame.sprite.Sprite.__init__(self)
        self.boot_im = pygame.image.load(f'src/image/boot/{boot_image}').convert_alpha()
        if type == 'up-down':
            self.boot_im_rc = self.boot_im.get_rect(center = (250, WS))
        elif type == 'left-right':
            self.boot_im_rc = self.boot_im.get_rect(center = (WS, 250))
        elif type == 'down-up':
            self.boot_im_rc = self.boot_im.get_rect(center = (250, WS+500))
        elif type == 'right-left':
            self.boot_im_rc = self.boot_im.get_rect(center = (WS+500, 250))

def win(boot_title, boot_ic, WIDTH, HEIGHT):
    '''создание окна и его значка с названием'''
    global window
    global W
    global H

    W = WIDTH
    H = HEIGHT

    programIcon = pygame.image.load(f'src/icon/{boot_ic}')
    pygame.display.set_icon(programIcon)
    window = pygame.display.set_mode((W,H))
    pygame.display.set_caption(f'{boot_title}')

def run_video():
    global duration
    global vid
    global confdatad

    for i in range(duration * 25):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        vid.draw(window, (0, 0), force_draw=False)
        time.sleep(0.03)
        clock.tick(FPS)
        pygame.display.flip()
    confdatad = True
    

def SPLASH(boot_image):
    '''создание статического логотипа на экране'''
    global window
    global boot_im
    global boot_im_rc

    boot_im = pygame.image.load(f'src/image/boot/{boot_image}')
    boot_im_rc = boot_im.get_rect(center = (W/2, H/2))
    window.blit(boot_im, boot_im_rc)

def VIDEO(video):
    global vid
    global duration
    clip = VideoFileClip(f"src/video/boot/{video}")
    duration = int(clip.duration)
    vid = Video(f"src/video/boot/{video}")
    vid.set_size((W,H))
    run_video()

def ANIMATE(boot_image, type, speed):
    '''создание динамического логотипа на экране'''
    global window
    global boot_im
    global boot_im_rc 
    global EnableAnimate
    global al
    global speedS

    speedS = speed
    al = animate_logo(WS = 0, boot_image=boot_image, type = type)
    if type == 'up-down':
        EnableAnimate = 1
    elif type == 'left-right':
        EnableAnimate = 2
    elif type == 'down-up':
        EnableAnimate = 3
        speedS = -speed
    elif type == 'right-left':
        EnableAnimate = 4
        speedS = -speed

def emit_particle(x_par, y_par, x_par_vel, y_par_vel, par_radius):
    particles.append([[x_par, y_par],[x_par_vel, y_par_vel], par_radius])

def update_particles(effect):
    for i, particle in reversed(list(enumerate(particles))):
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 1

        reversed_particle = particles[len(particles) - i - 1]
        image_effect_copy = pygame.transform.scale(effect, (particle[2], particle[2]))
        window.blit(image_effect_copy, (int(reversed_particle[0][0]), int(reversed_particle[0][1])))

        if particle[2] <= 0:
            particles.pop(i)

def EFFECT(status, image_effect):
    '''создание эффекта для логотипа. Не рекомендуется использовать статический'''
    global EnableEffect
    global particles
    global effect

    if status == 'disable':
        pass
    elif status == 'enable':
        EnableEffect = 1
        effect = pygame.image.load(f'src/effect/boot/{image_effect}')

def MUSIC():
    '''проигрывание музыки'''
    try:
        pygame.mixer.music.play()
    except:
        pass

def run():
    '''запуск загрузчика'''
    global boot_active
    global EnableAnimate
    global EnableEffect
    global al
    global vid
    global confdatad
    
    boot_active = True
    while boot_active:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        clock.tick(FPS)

        if EnableAnimate == 1:
            window.blit(al.boot_im, al.boot_im_rc)
            print(al.boot_im_rc.y)

            if al.boot_im_rc.y == 250:
                al.boot_im_rc.y = 250
            else:
                al.boot_im_rc.y += speedS
        elif EnableAnimate == 2:
            window.blit(al.boot_im, al.boot_im_rc)
            print(al.boot_im_rc.x)

            if al.boot_im_rc.x == 200:
                al.boot_im_rc.x = 200
            else:
                al.boot_im_rc.x += speedS
        elif EnableAnimate == 3:
            window.blit(al.boot_im, al.boot_im_rc)
            print(al.boot_im_rc.y)

            if al.boot_im_rc.y == 250:
                al.boot_im_rc.y = 250
            else:
                al.boot_im_rc.y += speedS
        elif EnableAnimate == 4:
            window.blit(al.boot_im, al.boot_im_rc)
            print(al.boot_im_rc.x)

            if al.boot_im_rc.x == 200:
                al.boot_im_rc.x = 200
            else:
                al.boot_im_rc.x += speedS
        else:
            pass
        if EnableEffect == 1:
            emit_particle(250, 250, random.uniform(-15, 15), random.uniform(-15, 15), 25)
            update_particles(effect=effect)
        elif EnableEffect == 0:
            pass

        if confdatad == True:
            import game
            pygame.quit()
        else:
            pass
        pygame.display.flip()
        
