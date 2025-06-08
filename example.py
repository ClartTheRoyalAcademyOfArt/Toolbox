
import random

import pygame

import toolbox





class GameWithToolbox(toolbox.Game):

    def __init__(self):
        super().__init__()

        self.win = toolbox.Window()
        self.event = toolbox.EventManager()

        self.renderer = toolbox.Renderer()
        self.renderer.create_queue("squares")
        
        self.timers = toolbox.TimerManager()
        self.stopwatches = toolbox.StopwatchManager()

        self.add_pre_frame_update_batch(
            (self.event.poll, 0),
            (lambda: self.event.handle_event(pygame.QUIT, self.quit_game), 1),
            (self.win.clear, 2),
            (self.timers.tick_all, 2)
        )

        self.add_post_frame_update(self.win.cycle, 0)


        self.timers.create_timer("debug_out", 5.0, self.debug, True)
        self.timers.create_timer("generate_square", 1.0, self.generate_square, True)

        self.stopwatches.create_new_stopwatch("window_runtime", True)
        self.stopwatches.create_new_stopwatch("render_time", True)


        self.squares = []
        self.render_time = 0
    


    def generate_square(self):

        square = pygame.Surface(( random.randint(10, 50),  random.randint(10, 50)))
        square.fill((random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))
        self.squares.append((square, (random.randint(0, 1280), random.randint(0, 720))))

        self.timers.timers["generate_square"].reset(True)
    


    def debug(self):

        print(f"Runtime: {self.stopwatches.get_time_elapsed("window_runtime"):.2f}")
        self.timers.timers["debug_out"].reset(True)

        print(f"Render time: {self.render_time:.10f}")
    


    def update(self):
        
        self.stopwatches.stopwatches["render_time"].reset(True)

        for square in self.squares:
            self.renderer.queue("squares", square[0], square[1])

        self.renderer.render(self.win.DISPLAY, "squares")

        self.render_time = self.stopwatches.stopwatches["render_time"].stop()





GameWithToolbox().run()