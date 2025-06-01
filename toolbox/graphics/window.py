
import time

import pygame





class Window:
    
    def __init__(self, size:tuple=(1280, 720), flags:int=0, frame_rate:int=60):
        
        pygame.display.init()

        self.size = size
        self.flags = flags
        self.frame_rate = frame_rate

        self.DISPLAY = pygame.display.set_mode(self.size, self.flags)

        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0

    

    def reload_display(self, size:tuple=(1280, 720), flags:int=0, frame_rate:int=60):

        pygame.display.init()

        self.size = size
        self.flags = flags
        self.frame_rate = frame_rate

        self.DISPLAY = pygame.display.set_mode(self.size, self.flags)

        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0
    


    @property
    def dt(self):

        return self.delta_time



    @property
    def fps(self):

        return self.CLOCK.get_fps()



    def clear(self, fill_color:tuple[int, int, int]=(20, 20, 20)):

        self.DISPLAY.fill(fill_color)
    


    def cycle(self):

        pygame.display.update()
        self.delta_time = self.CLOCK.tick(self.frame_rate) / 1000