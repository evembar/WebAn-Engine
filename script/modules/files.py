import script.modules.files_loader as fileloader

def background_menu(width, height):
    background = [fileloader.load_image("background/menu.jpg",width, height),
                  fileloader.load_image("background/menu1.jpg",width, height),
                  fileloader.load_image("background/menu2.jpg",width, height),
                  fileloader.load_image("background/menu3.jpg",width, height),
                  fileloader.load_image("background/menu4.jpg",width, height),
                  fileloader.load_image("background/menu5.jpg",width, height),
                  fileloader.load_image("background/menu6.jpg",width, height),
                  fileloader.load_image("background/menu7.jpg",width, height)]
    return background

def background_settings(width, height):
    background = [fileloader.load_image('background/settings.jpg', width, height),
                  fileloader.load_image('background/settings1.jpg', width, height),
                  fileloader.load_image('background/settings2.jpg', width, height),
                  fileloader.load_image('background/settings3.jpg', width, height),
                  fileloader.load_image('background/settings4.jpg', width, height),
                  fileloader.load_image('background/settings5.jpg', width, height),
                  fileloader.load_image('background/settings6.jpg', width, height)]
    return background

def menu_text():
    font = fileloader.load_font('font/lucidaconsole.ttf', 60)
    font1 = fileloader.load_font('font/lucidaconsole.ttf', 40)

    text = font.render("Обреченное поколение", 1, (255,255,255))
    text1 = font.render('Играть',1,(255,255,255))
    text2 = font1.render('Настройки',1,(255,255,255))
    text3 = font.render('Выход',1,(255,255,255))

    return [text, text1, text2, text3]

def settings_text():
    font = fileloader.load_font('font/lucidaconsole.ttf', 60)
    font1 = fileloader.load_font('font/lucidaconsole.ttf', 40)

    text = font.render("Настройки", 1, (255,255,255))
    text1 = font.render("Назад", 1, (255,255,255))
    text2 = font1.render("Полноэкранный режим:", 1, (255,255,255))
    text3 = font1.render("Музыка:", 1, (255,255,255))
    text4 = font1.render("Вкл", 1, (255,255,255))
    text5 = font1.render("Выкл", 1, (255,255,255))

    return [text, text1, text2, text3, text4, text5]

def button_standart():
    
    button = [fileloader.load_image('sprite/button/off.png', 300, 150),
                fileloader.load_image('sprite/button/on.png', 300, 150)]
    
    return button

def button_medium():

    button = [fileloader.load_image('sprite/button/off.png', 250, 125),
                fileloader.load_image('sprite/button/on.png', 250, 125)]
    
    return button

def button_small():

    button = [fileloader.load_image('sprite/button/off.png', 125, 63),
                fileloader.load_image('sprite/button/on.png', 125, 63)]
    
    return button

def video_logo(file, width, height):
    video = fileloader.load_video(file, width, height)

    return video

def profile_fetch(file):
    profile = fileloader.load_image(file, 450, 500)

    return profile

def profile_text():
    font = fileloader.load_font('font/lucidaconsole.ttf', 30)
    font1 = fileloader.load_font('font/lucidaconsole.ttf', 20)

    text = font.render("Новая", 1, (255,255,255))
    text1 = font1.render("Загрузка", 1, (255,255,255))
    text2 = font.render("Назад", 1, (255,255,255))
    text3 = font.render("Ввод", 1, (255,255,255))
    text4 = font.render("Готово", 1, (255,255,255))

    return [text, text1, text2, text3, text4]

def render_text(text, size, color):
    font = fileloader.load_font('font/lucidaconsole.ttf', size)
    text = font.render(text, 1, color)
    return text