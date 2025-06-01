
import pygame



class Renderer:

    def __init__(self):
        
        self.render_queues = {}
    


    def create_queue(self, queue_id:str):

        self.render_queues[queue_id] = {}



    def delete_queue(self, queue_id:str):

        del self.render_queues[queue_id]
    


    def get_queue(self, queue_id:str=None, return_all=False):

        if return_all:
            return self.render_queues
        
        return self.render_queues[queue_id]
    


    def queue(self, queue_id:str, surface:pygame.Surface, position:tuple[int, int], z_layer:int=0):

        key = z_layer

        if key not in self.render_queues[queue_id]:
            self.render_queues[queue_id][key] = []
        
        self.render_queues[queue_id][key].append((surface, position))



    def render(self, render_display:pygame.Surface, queue_id:str):

        for z in sorted(self.render_queues[queue_id].keys()):
            for surface, position in self.render_queues[queue_id][z]:
                render_display.blit(surface, position)
            
        self.render_queues[queue_id].clear()