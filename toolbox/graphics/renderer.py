
import pygame



class Renderer:

    def __init__(self):
        
        self._render_queues = {}
    


    def create_queue(self, queue_id:str) -> None:
        """
        Create a new queue

        queue_id : string id for new queue
        """

        self._render_queues[queue_id] = {}



    def delete_queue(self, queue_id:str) -> None:
        """
        Delete specified queue

        queue_id : queue to delete
        """

        del self._render_queues[queue_id]
    


    def get_queue(self, queue_id:str=None, return_all=False) -> dict:
        """
        Returns specified OR all queues

        queue_id : if not None, queue to return
        return_all : if True, returns all queues
        """

        if return_all:
            return self._render_queues
        
        return self._render_queues[queue_id]
    


    def queue(self, queue_id:str, surface:pygame.Surface, position:tuple[int, int], z_layer:int=0) -> None:
        """
        Queue a surface for render

        queue_id : queue to queue surface to
        surface : surface to queue
        position : position to render surface to
        z_layer : z order for rendering
        """

        key = z_layer

        if key not in self._render_queues[queue_id]:
            self._render_queues[queue_id][key] = []
        
        self._render_queues[queue_id][key].append((surface, position))



    def render(self, render_display:pygame.Surface, queue_id:str) -> None:
        """
        Blits surfaces of the passed queue to the passed surface

        render_display : pygame.Surface to blit to
        queue_id : queue to blit
        """
        
        for z in sorted(self._render_queues[queue_id].keys()):
            for surface, position in self._render_queues[queue_id][z]:
                render_display.blit(surface, position)
            
        self._render_queues[queue_id].clear()