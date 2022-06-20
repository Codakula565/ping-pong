from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGroupBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wigth, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wigth, height))
        self.speed = player_speed
        self.rect = self.image.getrect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def recet(self):
        w.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y<w_height-80:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<w_height-80:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        


#app = QApplication([])

back = (200,255,255)
w_width = 600
w_height = 500

w = display.set_mode((w_width,w_height))


#w.setWindowTitle('Pin ponge')

w.fill(back)

game=True
finish=False
clock=time.Clock()
FPS = 60

while True:
    display.update()
    clock.tick(FPS)
#w.show()
#app.exec_()