import pygame

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
screen_width = 1024
screen_height = 1024

# Создаем окно
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простой экран с Pygame")

#Шаг 1 - загрузка изображения
labirint = pygame.image.load("Картинки_для_лабиринта/начальная_картинка_лабиринта.png")

#Шаг 1 - загрузка будущей кнопки
button_play = pygame.image.load("Картинки_для_лабиринта/button_play.png")
button_exit = pygame.image.load("Картинки_для_лабиринта/button_exit.png")

labirint_MY = pygame.image.load("Картинки_для_лабиринта/labirint_MY.png")
labirint_MY = pygame.transform.scale(labirint_MY, (1024, 1024))

person_game1 = pygame.image.load("bat_costuims/bat-a.png")
person_game1 = pygame.transform.scale(person_game1, (60, 40))
person_game2 = pygame.image.load("bat_costuims/bat-b.png")
person_game3 = pygame.image.load("bat_costuims/bat-c.png")
person_game4 = pygame.image.load("bat_costuims/bat-d.png")



player_width = 10
player_height = 10

person_game1_x = 945
person_game1_y = 950

#Шаг 2 - создаю прямоугольник с координатами и размерами
button_play_rect = pygame.Rect(470, 450, 350, 350)

# Основные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

numbers_of_screen = 1  #переменная для изменения виджетов между собой

b = 0
a = 1

# Основной цикл программы
while a != b:
    #цикл while - проверяет ДЕЙСТВИЯ
    last_update_time = pygame.time.get_ticks()
    #print(last_update_time)
    for event in pygame.event.get():  # Правильный вызов
        #цикл FOR - проверет События

        #print(event)
        if event.type == pygame.QUIT:
            b = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and numbers_of_screen == 1:
            x = event.pos[0]
            y = event.pos[1]
            if 470 <= x <= 570 and 450 <= y <= 550:
                numbers_of_screen = 2

            print(event.pos)  #обратились к параметру pos у события  MOUSEBUTTONDOWN
            print("Вы нажали на кнопку", numbers_of_screen)



        elif event.type == pygame.KEYDOWN and numbers_of_screen == 2:  #если event заметил событие (нажатие клавиатуры)и это экран 2 значит выполнять следующее действие
            print(event.key, "Вы нажали клавишу!")
            if event.key == 1073741906:  #обратились к параметру key у кнопки
                print("вы нажали стрелку вверх!")
                person_game1_y -= 10
            elif event.key == 1073741905:
                person_game1_y += 10
            elif event.key == 1073741904:
                person_game1_x -= 10
            elif event.key == 1073741903:
                for x in range (person_game1_x,person_game1_x + player_width):
                  for y in range (person_game1_y,person_game1_y + player_height):

                    print(x,y)
                    if labirint_array [x,y] == labirint_MY.map_rgb((0,0,0)):
                        print("я не могу пройти")
                        print(False)
                        break

                person_game1_x += 10


    # Заливка экрана белым цветом
    screen.fill(WHITE)

    if numbers_of_screen == 1:  #запускаем виджеты первого фрейма если numbers_of_screen ==1
        # Шаг 2 - размещение изображения на экране
        screen.blit(labirint, (0, 0))  #

        # Шаг 3 - размещаю картинку в созданном прямоугольнике
        screen.blit(button_play, button_play_rect.topleft)

    elif numbers_of_screen == 2:
        labirint_array = pygame.PixelArray(labirint_MY)
        #if labirint_array[255,531] == labirint_MY.map_rgb((255,255,255)):#проверяем пиксель определённой координаты на белый цвет
          #print("Белый УРА!")
        labirint_array.close()

        screen.blit(labirint_MY, (0, 0))

        screen.blit(person_game1, (person_game1_x, person_game1_y))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
