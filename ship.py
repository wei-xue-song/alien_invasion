import pygame
from pygame import Surface
from pygame.sprite import Sprite

from settings import Settings


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, screen: Surface, settings: Settings) -> None:
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        # 加载飞船的图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.center_ship()

        # 移动标志
        self.moving_left = False
        self.moving_right = False

    def center_ship(self):
        """让飞船在屏幕底部居中"""
        # 对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blit_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
