import  pygame
import os
def load_tmx_map():
    #создаём поверхность для карты
    map_width = 32
    map_height = 32
    tile_size = 32
    map_surface = pygame.Surface((map_width * tile_size , map_height * tile_size))
    map_surface.fill((200 , 230 , 255))