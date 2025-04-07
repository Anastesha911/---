import pygame
import pytmx  # Библиотека для работы с TMX-картами


def load_tmx_map():
    # Загружаем TMX-файл с помощью pytmx
    tmx_data = pytmx.load_pygame("map_hard/level_1.tmx")

    # Получаем размеры карты в пикселях (умножаем количество тайлов на размеры тайлов)
    map_width = tmx_data.width * tmx_data.tilewidth
    map_height = tmx_data.height * tmx_data.tileheight

    # Создаём поверхность для карты
    map_surface = pygame.Surface((map_width, map_height))
    map_surface.fill((200, 230, 255))  # Добавляем светло-голубой цвет фону

    # Получаем список индексов слоёв
    layer_indices = []
    for i, layer in enumerate(tmx_data.visible_layers):
        if isinstance(layer, pytmx.TiledTileLayer):
            layer_indices.append(i)

    # Проходим по всем тайлам каждого слоя
    for layer_idx in layer_indices:
        for x in range(0, tmx_data.width):
            for y in range(0, tmx_data.height):
                # Получаем изображение на данной позиции, используя индекс слоя
                tile = tmx_data.get_tile_image(x, y, layer_idx)
                # Если тайл существует, рисуем его
                if tile:
                    # Рассчитываем позицию тайла на карте
                    pos_x = x * tmx_data.tilewidth
                    pos_y = y * tmx_data.tileheight
                    # Размещаем тайл на карте
                    map_surface.blit(tile, (pos_x, pos_y))

    # Возвращаем созданную поверхность
    return map_surface
