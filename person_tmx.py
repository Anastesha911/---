import pygame#импортировали библиотеку pygame


class Person ():#создали класс Person
    def __init__(self,x,y,size_width,size_height):#Конструктор класса (определили характеристики объектов класса)
        self.speed = 3#статестический параметр
        self.size_width = size_width#динамический параметр
        self.size_height = size_height#динамический параметр
        self.jump = 10#статестический параметр
        self.x = x#динамический параметр
        self.y = y#динамический параметр
        self.rect = pygame.Rect(self.size_width,self.size_height,x,y)#динамический параметр

    def draw_rect (self,screen):#создали метод draw_rect
        pygame.draw.rect(screen,(1,1,1),self.rect)#создали объект rect(прямоугольник)
