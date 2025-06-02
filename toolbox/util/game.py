
from sys import exit
from pygame import quit



class Game:

    def __init__(self):
        
        self.running = False

    

    def update(self):
    
        pass



    def quit_game(self):

        quit()
        exit()



    def run(self):
        """
        Run game loop
        """

        self.running = True

        while self.running:
            self.update()