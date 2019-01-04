# alien_invasion
python pygame one test




### 增加发射子弹功能(2018.1.4)
#### 使用精灵类(Sprite)
一般通过继承Sprite的形式来使用Sprite类
```
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #在子类初始化函数中，调用父类初始化函数
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
```
#### 使用精灵类组(Group)
多个类对象可以放入精灵组中操作,使用Group类
```
from pygame.sprite import Group

#创建一个用于存储子弹的编组
#Group类类似与列表，但提供了有助于游戏开发的额外功能
bullets = Group()

#添加精灵到组
new_bullet = Bullet(ai_settings, screen, ship)
bullets.add(new_bullet)

#对精灵组内成员进行操作（浅copy）
for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
```

### python浅拷贝、深拷贝

[直接赋值、浅拷贝、深拷贝](http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html)


