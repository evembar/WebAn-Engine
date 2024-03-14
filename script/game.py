import script.modules.ascii_logo
import pygame
import sys
import os
import script.data.settings as settings_data
import script.modules.files as files
from random import randint
import time

print('WebAn: Inizialisation')

run = False

pygame.init()
pygame.mixer.init()

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.display.set_icon(pygame.image.load('icon/icon.bmp'))
pygame.display.set_caption('DOOMED GENERATION')

width=1280
height=680
fps_timer = pygame.time.Clock()
fps = 60
fullscreen_switch = settings_data.fullscreen
sound_switch = settings_data.music
screenfetch = pygame.display.Info()

if fullscreen_switch == True:
    screen = pygame.display.set_mode((screenfetch.current_w,screenfetch.current_w), pygame.FULLSCREEN, vsync=1)
if fullscreen_switch == False:
    screen = pygame.display.set_mode((width,height), pygame.RESIZABLE, vsync=1)

pygame.mixer.music.set_volume(sound_switch) 
screen.blit(pygame.transform.scale(pygame.image.load('logo/weban.png'), (width, height)), (0,0))
pygame.display.flip()

print('WebAn: Load post objects')

menu_background_image = files.background_menu(width, height)
settings_background_image = files.background_settings(width, height)
menu_text = files.menu_text()
settings_text = files.settings_text()
button_standart = files.button_standart()
button_medium = files.button_medium()
button_small = files.button_small()
video_logo = files.video_logo(f'video/intro_walm{randint(0,1)}.mp4', width, height)
video_logo.set_volume(sound_switch)
profile_fetch = files.profile_fetch('sprite/human_information.png')
profile_text = files.profile_text()

current_size_window = screen.get_size()
last_size_window = current_size_window
virtual_surface = pygame.Surface((width, height))

menu_music = 1

current_scene = None
effect_current_scene = None

def switch_scene(scene):
    global current_scene
    current_scene = scene

def profile():
    global current_size_window, fullscreen_switch, screen, virtual_surface, last_size_window, effect_current_scene

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('music/kelochki.ogg')
    pygame.mixer.music.play(-1)

    input_text = 0
    input_name = ''
    input_surname = ''
   
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_size_window = event.size
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if input_text == 1:
                    if event.key == pygame.K_RETURN:
                        input_text = 0
                    elif event.key == pygame.K_BACKSPACE:
                        input_name = input_name[:-1]
                    else:
                        if len(input_name) < 17:
                            input_name += event.unicode
                if input_text == 2:
                    if event.key == pygame.K_RETURN:
                        input_text = 0
                    elif event.key == pygame.K_BACKSPACE:
                        input_surname = input_surname[:-1]
                    else:
                        if len(input_name) < 17:
                            input_surname += event.unicode



        SurfX, SurfY = current_size_window[0]/100, current_size_window[1]/100

        mouse = pygame.mouse.get_pressed()
        mouseX, mouseY = pygame.mouse.get_pos()

        adapt_X = (width/100)/SurfX
        adapt_y = (height/100)/SurfY

        virtual_surface.fill("black")

        virtual_surface.blit(profile_fetch, (400, 100))

        virtual_surface.blit(button_small[0], (415,520))
        virtual_surface.blit(button_small[0], (565,520))
        virtual_surface.blit(button_small[0], (715,520))

        virtual_surface.blit(profile_text[0], (436, 538))
        virtual_surface.blit(profile_text[1], (586, 538))
        virtual_surface.blit(profile_text[2], (736, 538))

        if mouse == (False, False, False):
            if mouseX >= 415/adapt_X and mouseX <= 540/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    virtual_surface.blit(button_small[1], (415,520))
                    virtual_surface.blit(profile_text[0], (436, 538))
            elif mouseX >= 565/adapt_X and mouseX <= 690/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    virtual_surface.blit(button_small[1], (565,520))
                    virtual_surface.blit(profile_text[1], (586, 538))
            elif mouseX >= 715/adapt_X and mouseX <= 830/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    virtual_surface.blit(button_small[1], (715,520))
                    virtual_surface.blit(profile_text[2], (736, 538))

            if mouseX >=410/adapt_X and mouseX <= 830/adapt_X:
                if mouseY >= 260/adapt_y and mouseY <=313/adapt_y:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
                elif mouseY >= 360/adapt_y and mouseY <=413/adapt_y:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                
        if mouse == (True, False, False):
            if mouseX >= 415/adapt_X and mouseX <= 540/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    sys.exit()
            elif mouseX >= 565/adapt_X and mouseX <= 690/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    sys.exit()
            elif mouseX >= 715/adapt_X and mouseX <= 830/adapt_X:
                if mouseY >= 520/adapt_y and mouseY <= 583/adapt_y:
                    effect_current_scene = menu
                    switch_scene(scene_effect)
                    run = False

            if mouseX >=410/adapt_X and mouseX <= 830/adapt_X:
                if mouseY >= 260/adapt_y and mouseY <=313/adapt_y:
                    input_text = 1
                elif mouseY >= 360/adapt_y and mouseY <=413/adapt_y:
                    input_text = 2

        input_keys = pygame.key.get_pressed()
        
        render_name_text = files.render_text(input_name, 40, (255,255,255))
        virtual_surface.blit(render_name_text, (420, 270))

        render_surname_text = files.render_text(input_surname, 40, (255,255,255))
        virtual_surface.blit(render_surname_text, (420, 370))

        scaled_surface = pygame.transform.scale(virtual_surface, current_size_window)
        screen.blit(scaled_surface, (0,0))

        fps_timer.tick(fps)
        pygame.display.flip()

def scene_effect():
    global current_size_window, fullscreen_switch, screen, virtual_surface, last_size_window, effect_current_scene
    i = 255
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_size_window = event.size

        if i > 0:
            virtual_surface.fill((0+i, 0+i, 0+i))
            i -= 10
            time.sleep(0.0005)
        else:
            run = False
            switch_scene(effect_current_scene)

        scaled_surface = pygame.transform.scale(virtual_surface, current_size_window)
        screen.blit(scaled_surface, (0,0))

        fps_timer.tick(fps)
        pygame.display.flip()

def settings():
    global current_size_window, fullscreen_switch, screen, virtual_surface, last_size_window, fullscreen_switch, sound_switch, effect_current_scene
  
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('music/connect.ogg')
    pygame.mixer.music.play(-1)

    background_timer = 0
    background_number = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_size_window = event.size

        if background_timer >= 100:
            background_number +=1
            background_timer = 0

        if background_number == 0:
            background = settings_background_image[0]
        elif background_number == 6:
            background = settings_background_image[0]
            background_number = 0
        else:
            background = settings_background_image[background_number]

        virtual_surface.fill('black')
        virtual_surface.blit(background,(0,0))
        virtual_surface.blit(settings_text[0], (500, 50))
        virtual_surface.blit(settings_text[2], (150,200))
        virtual_surface.blit(settings_text[3], (150,270))

        if fullscreen_switch == True:
            virtual_surface.blit(settings_text[4], (643, 203))
        elif fullscreen_switch == False:
            virtual_surface.blit(settings_text[5], (643, 203))
        virtual_surface.blit(button_small[0], (625, 195))

        if sound_switch == True:
            virtual_surface.blit(settings_text[4], (337, 263))
        elif sound_switch == False:
            virtual_surface.blit(settings_text[5], (337, 263))
        virtual_surface.blit(button_small[0], (320, 255))

        virtual_surface.blit(button_medium[0], (950, 500))
        virtual_surface.blit(settings_text[1], (998, 535))

        SurfX, SurfY = current_size_window[0]/100, current_size_window[1]/100

        mouse = pygame.mouse.get_pressed()
        mouseX, mouseY = pygame.mouse.get_pos()

        adapt_X = (width/100)/SurfX
        adapt_y = (height/100)/SurfY

        if mouse == (False, False, False):
            if mouseX >= 950/adapt_X and mouseX <= 1200/adapt_X:
                if mouseY >=500/adapt_y and mouseY <= 600/adapt_y:
                    virtual_surface.blit(button_medium[1], (950, 500))
                    virtual_surface.blit(settings_text[1], (998, 535))
            if mouseX >= 625/adapt_X and mouseX <= 750/adapt_X:
                if mouseY >=195/adapt_y and mouseY <= 258/adapt_y:
                    virtual_surface.blit(button_small[1], (625, 195))
                    if fullscreen_switch == True:
                        virtual_surface.blit(settings_text[4], (643, 203))
                    elif fullscreen_switch == False:
                        virtual_surface.blit(settings_text[5], (643, 203))     
            if mouseX >= 320/adapt_X and mouseX <= 445/adapt_X:
                if mouseY >=255/adapt_y and mouseY <= 318/adapt_y:
                    virtual_surface.blit(button_small[1], (320, 255))
                    if sound_switch == True:
                        virtual_surface.blit(settings_text[4], (337, 263))
                    elif sound_switch == False:
                        virtual_surface.blit(settings_text[5], (337, 263))

        if mouse == (True, False, False):
            if mouseX >= 950/adapt_X and mouseX <= 1200/adapt_X:
                if mouseY >=500/adapt_y and mouseY <= 600/adapt_y:
                    run = False 
                    effect_current_scene = menu
                    switch_scene(scene_effect)
            if mouseX >= 625/adapt_X and mouseX <= 750/adapt_X:
                if mouseY >=195/adapt_y and mouseY <= 258/adapt_y:
                    if fullscreen_switch == True:
                        screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
                        pygame.time.delay(500)
                        fullscreen_switch = False
                        os.remove('script/data/settings.py')
                        settings_py = open('script/data/settings.py', "w+")
                        settings_py.write(f"fullscreen = {fullscreen_switch}\nmusic = {sound_switch}")
                        settings_py.close()
                        virtual_surface.blit(settings_text[5], (643, 203))
                    elif fullscreen_switch == False:
                        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        pygame.time.delay(500)
                        screen = pygame.display.set_mode((screenfetch.current_w,screenfetch.current_w), pygame.FULLSCREEN)
                        pygame.time.delay(500)
                        fullscreen_switch = True
                        os.remove('script/data/settings.py')
                        settings_py = open('script/data/settings.py', "w+")
                        settings_py.write(f"fullscreen = {fullscreen_switch}\nmusic = {sound_switch}")
                        settings_py.close()
                        virtual_surface.blit(settings_text[4], (643, 203)) 
            if mouseX >= 320/adapt_X and mouseX <= 445/adapt_X:
                if mouseY >=255/adapt_y and mouseY <= 318/adapt_y:
                    if sound_switch == True:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.0)
                        sound_switch = False
                        settings_py = open('script/data/settings.py', "w+")
                        settings_py.write(f"fullscreen = {fullscreen_switch}\nmusic = {sound_switch}")
                        settings_py.close()
                        virtual_surface.blit(settings_text[5], (337, 263))
                        time.sleep(0.1)
                        run = False
                    elif sound_switch == False:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(100.0)
                        sound_switch = True
                        settings_py = open('script/data/settings.py', "w+")
                        settings_py.write(f"fullscreen = {fullscreen_switch}\nmusic = {sound_switch}")
                        settings_py.close()
                        virtual_surface.blit(settings_text[4], (337, 263))
                        time.sleep(0.1)
                        run = False   

        scaled_surface = pygame.transform.scale(virtual_surface, current_size_window)
        screen.blit(scaled_surface, (0,0))

        fps_timer.tick(fps)
        background_timer +=1
        pygame.display.flip()

def menu():
    global current_size_window, fullscreen_switch, screen, virtual_surface, last_size_window, menu_music, effect_current_scene
    background_timer = 0
    background_number = 0
      
    if menu_music == 1:
        pygame.mixer.music.load('music/theme_doomer.ogg')
        pygame.mixer.music.play()
    elif menu_music == 2:
        pygame.mixer.music.load('music/fight.ogg')
        pygame.mixer.music.play()    

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_size_window = event.size
            elif event.type == MUSIC_END:
                if menu_music == 1:
                    menu_music = 2
                elif menu_music == 2:
                    menu_music = 1
                run = False
                switch_scene(menu)

        SurfX, SurfY = current_size_window[0]/100, current_size_window[1]/100

        adapt_X = (width/100)/SurfX
        adapt_y = (height/100)/SurfY

        if background_number == 0:
            background = menu_background_image[0]
        elif background_number == 8:
            background = menu_background_image[0]
            background_number = 0
        else:
            background = menu_background_image[background_number]

        if background_timer >= 100:
            background_number +=1
            background_timer = 0
        
        virtual_surface.fill('black')
        virtual_surface.blit(background, (0,0))
        virtual_surface.blit(menu_text[0], (316, 100))

        virtual_surface.blit(button_standart[0], (302, 240))
        virtual_surface.blit(menu_text[1], (350, 280))

        virtual_surface.blit(button_standart[0], (492, 420))
        virtual_surface.blit(menu_text[3], (570, 460))

        virtual_surface.blit(button_standart[0], (702, 240))
        virtual_surface.blit(menu_text[2], (750, 280))

        mouse = pygame.mouse.get_pressed()
        mouseX, mouseY = pygame.mouse.get_pos()

        if mouse == (False, False, False):
            if mouseX >= 302/adapt_X and mouseX <= 602/adapt_X:
                if mouseY >=240/adapt_y and mouseY <= 390/adapt_y:
                    virtual_surface.blit(button_standart[1], (302, 240))
                    virtual_surface.blit(menu_text[1], (350, 280))
            if mouseX >= 492/adapt_X and mouseX <= 792/adapt_X:
                if mouseY >=420/adapt_y and mouseY <= 570/adapt_y:
                    virtual_surface.blit(button_standart[1], (492, 420))
                    virtual_surface.blit(menu_text[3], (570, 460))
            if mouseX >= 702/adapt_X and mouseX <= 1002/adapt_X:
                if mouseY >=240/adapt_y and mouseY <= 390/adapt_y:
                   virtual_surface.blit(button_standart[1], (702, 240))
                   virtual_surface.blit(menu_text[2], (750, 280)) 

        #Работа адаптивных пикселей

        if mouse == (True, False, False):
            if mouseX >= 302/adapt_X and mouseX <= 602/adapt_X:
                if mouseY >=240/adapt_y and mouseY <= 390/adapt_y:
                    run = False
                    effect_current_scene = profile
                    switch_scene(scene_effect)
                    #function for button
            if mouseX >= 492/adapt_X and mouseX <= 792/adapt_X:
                if mouseY >=420/adapt_y and mouseY <= 570/adapt_y:
                    run = False 
                    effect_current_scene = sys.exit
                    switch_scene(scene_effect)
            if mouseX >= 702/adapt_X and mouseX <= 1002/adapt_X:
                if mouseY >=240/adapt_y and mouseY <= 390/adapt_y:
                    run = False 
                    effect_current_scene = settings
                    switch_scene(scene_effect)

        scaled_surface = pygame.transform.scale(virtual_surface, current_size_window)
        screen.blit(scaled_surface, (0,0))

        fps_timer.tick(fps)
        background_timer += 1
        pygame.display.flip()

def logo():
    global current_size_window, fullscreen_switch, screen, virtual_surface, effect_current_scene
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_size_window = event.size
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if video_logo.get_pos() >= 2:
                        video_logo.pause() 
                        effect_current_scene = menu
                        switch_scene(scene=scene_effect)
                        run = False 

        video_logo.draw(virtual_surface, (0,0))

        if video_logo.get_pos() >= 12.5:
            effect_current_scene = menu
            switch_scene(scene=scene_effect)
            run = False 

        scaled_surface = pygame.transform.scale(virtual_surface, current_size_window)
        screen.blit(scaled_surface, (0,0))
            
        fps_timer.tick(fps)
        pygame.display.flip()

switch_scene(logo)
while current_scene is not None:
    current_scene()
