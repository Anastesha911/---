import pygame



# Инициализация Pygame

pygame.init()



# Задаем размеры окна

screen_width =1024

screen_height = 1024


# Создаем окно

screen = pygame.display.set_mode((screen_width, screen_height))#размеры экрана поместили в кортеже - tuple

pygame.display.set_caption("Простой экран с Pygame")



# Загрузка изображений

labirint = pygame.image.load("Картинки_для_лабиринта/начальная_картинка_лабиринта.png")



button_play = pygame.image.load("Картинки_для_лабиринта/button_play.png")

button_exit = pygame.image.load("Картинки_для_лабиринта/button_exit.png")

labirint_level2 = pygame.image.load("Картинки_для_лабиринта/хогварц.png")

labirint_MY = pygame.image.load("Картинки_для_лабиринта/labirint_MY.png")

labirint_MY = pygame.transform.scale(labirint_MY, (screen_width, screen_height-12))#команда pygame.transform.scale - отвечает за изменение размеров картинки


player_width = 50

player_height = 30



# Создаем маску лабиринта

mask = pygame.mask.from_threshold(labirint_MY, (0, 0, 0), (1, 1, 1))

person_mask = pygame.mask.Mask((player_width,player_height),True)


# Персонаж

person_game1 = pygame.image.load("bat_costuims/bat-a.png")

person_game1 = pygame.transform.scale(person_game1, (player_width, player_height))



person_game1_x = 519

person_game1_y = 995


health = 3
# Кнопка

button_play_rect = pygame.Rect(475, 455, 100, 50)



# Основные цвета

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)



# Переменные

numbers_of_screen = 1 # Для переключения между экранами

running = True

move_right = move_left = move_up = move_down = False


new_x, new_y = person_game1_x, person_game1_y

# Основной игровой цикл

while running:
  # начало цикла for



  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      running = False

    elif event.type == pygame.MOUSEBUTTONDOWN and numbers_of_screen == 1:

      x, y = event.pos
      # collidepoint - автоматически синхронизируется с прямоугольником и кликом мыши для кнопки для установления промежуточного пространства для смены экранов
      if button_play_rect.collidepoint(x, y):
        numbers_of_screen = 2

    elif event.type == pygame.KEYDOWN and numbers_of_screen == 2:


        # Обновляем координаты персонажа


        if event.key == pygame.K_UP:
          move_up = True

        elif event.key == pygame.K_DOWN:
          move_down = True

        elif event.key == pygame.K_LEFT:

          move_left = True

        elif event.key == pygame.K_RIGHT:
          move_right = True

      # Проверяем столкновение с чёрными пикселями


    elif event.type == pygame.KEYUP and numbers_of_screen == 2:
        if event.key == pygame.K_RIGHT:
            move_right = False
        elif event.key == pygame.K_LEFT:
            move_left = False
        elif event.key == pygame.K_UP:
            move_up = False
        elif event.key == pygame.K_DOWN:
            move_down = False


    # конец цикла for

    # Проверяем столкновение с чёрными пикселями
    if numbers_of_screen == 2 and person_game1_x < 455 and person_game1_y < 10:
        numbers_of_screen = 3
  #код для цикла while

  if move_right:
      new_x += 5
  elif move_left :
      new_x -= 5
  elif move_up:
      new_y -= 5
  elif move_down:
      new_y += 5

  if mask.overlap(person_mask, (new_x, new_y)):  # с помощью команды overlap проверяются текущие координаты в person_mask и будущие new_x new_y
      if move_right:
          new_x -= 3
      elif move_left:
          new_x += 3
      elif move_up:
          new_y += 3
      elif move_down:
          new_y -= 3
      health -= 1
      new_x = person_game1_x
      new_y = person_game1_y
      print ("Минус сердечко! Осталось",health,"сердце")

  elif numbers_of_screen == 2 and person_game1_x < 450 and person_game1_y < 10:
        numbers_of_screen = 3
  else:
      person_game1_x, person_game1_y = new_x, new_y
      print(person_game1_x,person_game1_y)
      if person_game1_x < 450  and  person_game1_y < 10:
          print("Вы прошли!!!")

  # Заливка экрана

  screen.fill(WHITE)



  if numbers_of_screen == 1: # Экран с кнопкой

    screen.blit(labirint, (0, 0))

    pygame.draw.rect(screen, (200, 200, 200), button_play_rect)

    screen.blit(button_play, button_play_rect.topleft)

  elif numbers_of_screen == 2: # Лабиринт

    screen.blit(labirint_MY, (0, 0))

    screen.blit(person_game1, (person_game1_x, person_game1_y))
  elif numbers_of_screen == 3:
    screen.blit(labirint_level2,(0,0))


  # Обновляем экран

  pygame.display.flip()



# Завершаем Pygame