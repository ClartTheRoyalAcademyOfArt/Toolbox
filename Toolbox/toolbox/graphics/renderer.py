
import pygame



class Renderer:

    def __init__(self):
        
        self.render_queue = {}
    


    def get_queue(self):

        return self.render_queue
    


    def queue(self, surface:pygame.Surface, position:tuple[int, int], z_layer:int=0):

        key = z_layer

        if key not in self.render_queue:

            self.render_queue[key] = []
        
        self.render_queue[key].append((surface, position))



    def render(self, render_display:pygame.Surface):

        for z in sorted(self.render_queue.keys()):

            for surface, position in self.render_queue[z]:

                render_display.blit(surface, position)
            
        self.render_queue.clear()