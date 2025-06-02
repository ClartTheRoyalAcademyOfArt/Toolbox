
import time

import pygame





class Window:
    
    def __init__(self, size:tuple=(1280, 720), flags:int=0, frame_rate:int=60):
        """
        size : size of the pygame.display window
        flags : pygame.display flags
        frame_rate : pygame.display frame rate, passed to pygame.time.Clock.tick()
        """
        
        pygame.display.init()

        self.size = size
        self.flags = flags
        self.frame_rate = frame_rate

        self.DISPLAY = pygame.display.set_mode(self.size, self.flags)

        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0

    

    def reload_display(self, size:tuple=(1280, 720), flags:int=0, frame_rate:int=60):
        """
        Reloads the display with the passed values.

        size : size of the pygame.display window
        flags : pygame.display flags
        frame_rate : pygame.display frame rate, passed to pygame.time.Clock.tick()
        """

        pygame.display.init()

        self.size = size
        self.flags = flags
        self.frame_rate = frame_rate

        self.DISPLAY = pygame.display.set_mode(self.size, self.flags)

        self.CLOCK = pygame.time.Clock()
        self.delta_time = 0
    


    @property
    def dt(self):
        """
        Returns self.delta_time
        """

        return self.delta_time



    @property
    def fps(self):
        """
        Returns self.CLOCK.get_fps()
        """

        return self.CLOCK.get_fps()



    def clear(self, fill_color:tuple[int, int, int]=(20, 20, 20)):
        """
        Fills the display with the passed RGB values

        fill_color : tuple, (R, G, B)
        """

        self.DISPLAY.fill(fill_color)
    


    def cycle(self):
        """
        Updates the display, updates self.delta_time, cycles CLOCK
        """

        pygame.display.update()
        self.delta_time = self.CLOCK.tick(self.frame_rate) / 1000