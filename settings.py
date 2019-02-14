class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1100
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        #飞船的设置
        # self.ship_speed_factor = 0.8
        self.ship_limit = 3

        # 子弹的设置
        # self.bullet_speed_factor = 1
        self.bullet_width = 30
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        #外星人的设置
        self.fleet_drop_speed = 2

        # 以怎么的速度加快游戏节奏
        self.speedup_scale = 10

        self.initialize_dynamic_settings()

        # self.alien_speed_factor = 1
        # #fleet_direction为1表示向右移，为-1表示向左移
        # self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
