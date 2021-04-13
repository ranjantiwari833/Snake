from snake import Snake
from constants import *

class Obstacle(Snake):
    def __init__(self):
        self.body = []
        self.create_snake(cor= OBS_LOCATION[0])
    
    def second_obstacle(self):
        self.create_snake(cor= OBS_LOCATION[1])
    
    def third_obstacle(self):
        self.create_snake(cor= OBS_LOCATION[2])
    
    def fourth_obstacle(self):
        self.create_snake(cor= OBS_LOCATION[3])
    
    def fifth_obstacle(self):
        self.create_snake(cor= OBS_LOCATION[4])
    