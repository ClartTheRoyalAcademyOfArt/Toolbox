import sys

import pygame

import toolbox




class GameWithToolbox(toolbox.Game):

    def __init__(self):
        super().__init__()

        self.win = toolbox.Window()
        self.event = toolbox.EventManager()

        self.add_pre_frame_update_batch(
            (self.event.poll, 0),
            (lambda: self.event.handle_event(pygame.QUIT, self.quit_game), 1),
            (self.win.clear, 2)
        )

        self.add_post_frame_update(self.win.cycle, 0)










class GameWithoutToolbox:

    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 1280, 720
        self.DISPLAY = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.CLOCK = pygame.time.Clock()
        self.FPS = 60

        self.dt = 0
    


    def handle_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    


    def run(self):

        while True:
            self.DISPLAY.fill((20, 20, 20))

            self.handle_event()

            pygame.display.update()
            self.dt = self.CLOCK.tick(self.FPS) / 1000





GameWithToolbox().run()
# GameWithoutToolbox().run()