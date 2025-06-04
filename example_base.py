
import pygame

import toolbox


"""
This script launches a window, and handles the pygame.QUIT event.

Update function is not explicitly needed here because all logic is
being handled in the toolbox.Game run() loop.
"""


class G(toolbox.Game):

    def __init__(self):
        super().__init__()

        self.win = toolbox.Window()
        self.event = toolbox.EventManager()

        self.add_update_call_batch(
            (self.event.poll, 0),
            (lambda: self.event.handle_event(pygame.QUIT, self.quit_game), 1),
            (self.win.clear, 2),
            (self.win.cycle, 2)
        )
    

    
    def update(self):
        
        pass



G().run()