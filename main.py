import pygame as pg 
import sys

class Game:
    def __init__(self, window_size=(1200, 600)) -> None:
        self.WINDOW_SIZE = window_size
        self.WINDOW_WIDTH = self.WINDOW_SIZE[0]
        self.WINDOW_HEIGHT = self.WINDOW_SIZE[1]
        self.MAX_FPS = 60
        pg.init()
        pg.mixer.init()
        
        self.is_running = True

        self.screen = pg.display.set_mode(self.WINDOW_SIZE)
        pg.display.set_caption('Platform Game')
        
        self.clock = pg.time.Clock()


    def quit(self):
        pg.quit()
        sys.exit()

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def run(self):
        

        while self.is_running:
            self.handle_event()


            pg.display.update()
            self.clock.tick(self.MAX_FPS)


if __name__ == '__main__':
    game = Game()
    game.run()