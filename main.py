import pygame



# Инициализация Pygame

pygame.init()



# Задаем размеры окна

screen_width =1024

screen_height = 1024


# Создаем окно

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Простой экран с Pygame")



# Загрузка изображений

labirint = pygame.image.load("Картинки_для_лабиринта/начальная_картинка_лабиринта.png")



button_play = pygame.image.load("Картинки_для_лабиринта/button_play.png")

button_exit = pygame.image.load("Картинки_для_лабиринта/button_exit.png")



labirint_MY = pygame.image.load("Картинки_для_лабиринта/labirint_MY.png")

labirint_MY = pygame.transform.scale(labirint_MY, (1024, 1024))



# Создаем маску лабиринта

mask = pygame.mask.from_threshold(labirint_MY, (0, 0, 0), (1, 1, 1))



# Персонаж

person_game1 = pygame.image.load("bat_costuims/bat-a.png")

person_game1 = pygame.transform.scale(person_game1, (60, 40))



player_width = 60

player_height = 40



person_game1_x = 109

person_game1_y = 250



# Кнопка

button_play_rect = pygame.Rect(475, 455, 100, 50)



# Основные цвета

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)



# Переменные

numbers_of_screen = 1 # Для переключения между экранами

running = True



# Основной игровой цикл

while running:

  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      running = False

    elif event.type == pygame.MOUSEBUTTONDOWN and numbers_of_screen == 1:

      x, y = event.pos

      if button_play_rect.collidepoint(x, y):

        numbers_of_screen = 2

    elif event.type == pygame.KEYDOWN and numbers_of_screen == 2:

      # Обновляем координаты персонажа

      new_x, new_y = person_game1_x, person_game1_y



      if event.key == pygame.K_UP:

        new_y -= 10

      elif event.key == pygame.K_DOWN:

        new_y += 10

      elif event.key == pygame.K_LEFT:

        new_x -= 10

      elif event.key == pygame.K_RIGHT:

        new_x += 10



      # Проверяем столкновение с чёрными пикселями

      if mask.overlap_area(pygame.mask.Mask((player_width, player_height), True), (new_x, new_y)):

        print("Персонаж не может пройти, стена!")

      else:

        person_game1_x, person_game1_y = new_x, new_y



  # Заливка экрана

  screen.fill(WHITE)



  if numbers_of_screen == 1: # Экран с кнопкой

    screen.blit(labirint, (0, 0))

    pygame.draw.rect(screen, (200, 200, 200), button_play_rect)

    screen.blit(button_play, button_play_rect.topleft)

  elif numbers_of_screen == 2: # Лабиринт

    screen.blit(labirint_MY, (0, 0))

    screen.blit(person_game1, (person_game1_x, person_game1_y))



  # Обновляем экран

  pygame.display.flip()



# Завершаем Pygame