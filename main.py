#ООП Версия старого проекта


import arcade
import random
import draw
import fill
import update


SIDE = 900 #Пока что квадратное поле
PIXEL_SIDE = 2 #Размер одной клетки в пикселях





class GameWindow(arcade.Window):

    #Функция инициализации
    def __init__(self, width, height, title, pixel_side):
        super().__init__(width, height, title) #Шуры муры arcade'а
        # arcade.enable_timings() #Разрешаем задавать fps
        # arcade.get_fps(fps) #Задаём fps
        self.set_location(0, 0) #Располагаем окно
        arcade.set_background_color(arcade.color.BLACK) #Фон - чёрный

        #Объявляем все атрибуты
        self.width = width
        self.height = height
        self.columns = width // pixel_side
        self.lines = height // pixel_side
        self.pixel_side = pixel_side
        self.counter = 0 #Счетчик кадров

        self.BOARD = [[0 for _ in range(self.columns)] for _ in range(self.lines)] #Создание основного массива

        #Заполнение всех массивов
        fill_local = fill.main(self.lines, self.columns,self.BOARD)
        fill_local.cell(1000)



    #Функция отрисовки (ТУТ НЕЛЬЗЯ ДЕЛАТЬ РАСЧЁТЫ)2
    def on_draw(self):
        self.counter += 1 #Работа счетчика кадров
        arcade.start_render()
        arcade.draw_text('Кадр: ' + str(self.counter), 2, self.height-20, (122, 122, 122), 15) #Вывод счетчика

        draw_local = draw.main(self.lines, self.columns, self.pixel_side, self.BOARD)
        draw_local.draw()


    #Функция расчётов и всего подоного (по хорошому это всё должно быть в отдельном файле)
    def on_update(self, delta_time):
        update_local = update.main(self.lines, self.columns, self.pixel_side, self.BOARD)


#Запуск arcade
GameWindow(SIDE, SIDE, "ArcadeLife", PIXEL_SIDE)
arcade.run()