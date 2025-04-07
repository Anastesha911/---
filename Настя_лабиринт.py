
import pygame

from map_python import load_tmx_map

# Инициализация Pygame

pygame.init()

#Загружаем карту


#clock = pygame.time.Clock()
#print(clock)

# Задаем размеры окна

screen_width =1024

screen_height = 1024


# Создаем окно

screen = pygame.display.set_mode((screen_width, screen_height))#размеры экрана поместили в кортеже - tuple

pygame.display.set_caption("Простой экран с Pygame")

map_surface = load_tmx_map()


# Загрузка изображений

labirint = pygame.image.load("Картинки_для_лабиринта/начальная_картинка_лабиринта.png")



button_play = pygame.image.load("Картинки_для_лабиринта/button_play.png")

button_exit = pygame.image.load("Картинки_для_лабиринта/button_exit.png")

labirint_level2 = pygame.image.load("Картинки_для_лабиринта/хогварц.png")

labirint_MY = pygame.image.load("Картинки_для_лабиринта/labirint_MY.png")

labirint_MY = pygame.transform.scale(labirint_MY, (screen_width, screen_height-12))#команда pygame.transform.scale - отвечает за изменение размеров картинки


player_width = 50

player_height = 30

player_width2 = 150# ШИРИНА игрока
player_height2 = 150# ВЫСОТА игрока

# Создаем маску лабиринта

mask = pygame.mask.from_threshold(labirint_MY, (0, 0, 0), (1, 1, 1))

person_mask = pygame.mask.Mask((player_width,player_height),True)


# Персонаж

person_game1 = pygame.image.load("bat_costuims/bat-a.png")

person_game1 = pygame.transform.scale(person_game1, (player_width, player_height))


person_game1_x = 600

person_game1_y = 140

number_of_dragon_x = 50

number_of_dragon_y = 755

dragon_frame = [
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-a.png"),(player_width2,player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-b.png"),(player_width2,player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-c.png"),(player_width2,player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-d.png"),(player_width2, player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-e.png"), (player_width2, player_height2)),
]
dragon_frame1 = [
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-f.png"),(player_width2,player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-g.png"),(player_width2,player_height2)),
    pygame.transform.scale(pygame.image.load("bat_costuims/dragon-h.png"),(player_width2,player_height2)),
]
number_of_dragon = 0
animation_spend = 100
frame_count = 0



#health = 3
# Кнопка

button_play_rect = pygame.Rect(475, 455, 100, 50)

#test_play_rect = pygame.Rect(0,0,1024,1024)

# Основные цвета

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)



# Переменные

numbers_of_screen = 1 # Для переключения между экранами

running = True

move_right = move_left = move_up = move_down = False


new_x, new_y = person_game1_x, person_game1_y

# Основной игровой цикл

# Основной игровой цикл
while running:
    #  ЭТАП 1  - Обработка событий
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if  numbers_of_screen == 1:
                #if event.pos[0] >= 475 and event.pos[0] <= 575 and 455 <= event.pos[1] <= 505 :

                if button_play_rect.collidepoint(event.pos):
                    numbers_of_screen = 2
            elif numbers_of_screen == 3:
                #print(event.pos)
                if 649  <= event.pos[0] <= 951 and 595 <= event.pos[1] <= 951:
                    numbers_of_screen = 4


        elif numbers_of_screen == 2:
            #Проверяется нажата ли клавиша
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                #Провряется была ли клавиша отпущена
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                #конец цикла for
    #ЭТАП 2 - обновление переменных
    # Движение персонажа
    if numbers_of_screen == 2:
        if move_right:
            new_x += 5
        elif move_left:
            new_x -= 5
        elif move_up:
            new_y -= 5
        elif move_down:
            new_y += 5

        # Проверка столкновения с лабиринтом
        if mask.overlap(person_mask, (new_x, new_y)):
            if move_right:
                new_x -= 3
            elif move_left:
                new_x += 3
            elif move_up:
                new_y += 3
            elif move_down:
                new_y -= 3



            #health -= 1
            new_x, new_y = person_game1_x, person_game1_y
            #print("Минус сердечко! Осталось", health, "сердце")

        else:
            person_game1_x, person_game1_y = new_x, new_y
            #print(person_game1_x, person_game1_y)


    #ЭТАП 3 - отображение игрового процесса
    # Отрисовка экрана
    screen.fill(WHITE)

    if numbers_of_screen == 1:  # Экран с кнопкой
        screen.blit(labirint, (0, 0))
        pygame.draw.rect(screen, (200, 200, 200), button_play_rect)
        screen.blit(button_play, button_play_rect.topleft)
      #  pygame.draw.rect(screen,(200,200,200),test_play_rect)

    elif numbers_of_screen == 2:  # Лабиринт
        screen.blit(labirint_MY, (0, 0))
        screen.blit(person_game1, (person_game1_x, person_game1_y))

        # Проверка выхода из лабиринта
        if person_game1_x < 450 and person_game1_y < 10 and numbers_of_screen == 2:
            numbers_of_screen = 3
            print("Вы прошли!!!")

    elif numbers_of_screen == 3:
        screen.blit(labirint_level2, (0, 0))
        screen.blit(dragon_frame [number_of_dragon],(number_of_dragon_x, number_of_dragon_y))
        frame_count += 1
        if frame_count > 100:
            frame_count = 0
        if frame_count == animation_spend:
            number_of_dragon += 1
            print (number_of_dragon)
        if number_of_dragon > 4:
            number_of_dragon = 0
        if number_of_dragon_x < 730 and number_of_dragon_y > 100 :
            number_of_dragon_x += 0.5
            number_of_dragon_y -= 0.5
        if number_of_dragon_x == 730 or number_of_dragon_y == 100:
            number_of_dragon=0
            screen.blit(dragon_frame1[number_of_dragon], (number_of_dragon_x, number_of_dragon_y))
            frame_count += 1
            if frame_count > 100:
                frame_count = 0
            if frame_count == animation_spend:
                number_of_dragon += 1
            if number_of_dragon > 2:
                number_of_dragon = 0

    elif numbers_of_screen == 4:
        screen.blit(map_surface , (0,0))
        person_game1_x = 500
        person_game1_y = 500
        screen.blit(person_game1,(person_game1_x,person_game1_y))

    pygame.display.flip()

# Завершаем Pygame
pygame.quit()# Завершаем Pygame
#ДОБАВИЛА КОМЕНТАРИЙ