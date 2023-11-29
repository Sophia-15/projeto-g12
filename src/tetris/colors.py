class Colors:
    dark_green = (1,50,32)
    green = (47,230,23)
    red = (232,18,18)
    pink = (255,74,174)
    yellow = (237,234,4)
    purple = (166,0,247)
    cyan = (21,204,209)
    blue = (13,64,216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    black = (0, 0, 0)
    yellow_m = (162, 136, 59)
    ciano_blue = (49, 201, 176)
    

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_green,cls.green,cls.red,cls.pink,cls.yellow,cls.purple,cls.cyan,cls.blue,cls.black,cls.yellow_m,cls.ciano_blue]