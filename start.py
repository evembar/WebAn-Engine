from engine import load
from engine import boot

class BOOT_FILES:
    load.init()
    load.font(boot_font='determination.otf')
    load.icon(boot_icon = 'logo.ico')
    load.music(boot_music = 'logo.mp3')

BOOT_FILES

class BOOT_START:
    #load.init_win(boot_title = 'WebAn')
    #boot.MUSIC()
    #boot.SPLASH(boot_image = 'logo.png')
    #boot.ANIMATE(boot_image = 'logo.png', type = 'up-down', speed = 2)
    #boot.ANIMATE(boot_image = 'logo.png', type = 'left-right', speed =2)
    #boot.ANIMATE(boot_image='logo.png',type='down-up',speed=2)
    #boot.ANIMATE(boot_image='logo.png',type='right-left',speed=2)
    #boot.EFFECT(status='enable', image_effect='star.png')
    #load.run()
    pass

#BOOT_START

class BOOT_VIDEO:
    load.init_win(boot_title = 'WebAn', WIDTH = 1080, HEIGHT = 500)
    boot.VIDEO(video = 'weban.mp4')
    load.run()

BOOT_VIDEO
