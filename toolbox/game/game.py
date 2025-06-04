
from typing import Callable

from sys import exit
from pygame import quit



class Game:

    def __init__(self):
        
        self._running = False

        self._update_calls = []

    

    def add_update_call(self, update_call:Callable[[], None], priority:int=0) -> None:
        """
        Adds a function to the update queue with a given priority. 0 is a higher priority than 1.

        update_call : Callable to add to the update queue
        priority : integer representation of the callable's priority
        """

        self._update_calls.append((priority, update_call))
        self._update_calls.sort(key=lambda item: item[0])
    


    def add_update_call_batch(self, *update_calls:tuple[Callable[[], None], int]) -> None:
        """
        Adds multiple update calls at once. Each call is a (callable, priority) tuple.

        update_calls : list of update calls in format (callable, priority)
        """

        for func, priority in update_calls:
            self.add_update_call(func, priority)


    
    def remove_update_call(self, update_call: Callable[[], None]) -> None:
        """
        Removes all instances of the given callable from the queue.

        update_call : Callable to remove from the queue
        """

        self._update_calls = [(priority, func) for (priority, func) in self._update_calls if func != update_call]

    

    def update(self) -> None:
        """
        Update loop.
        """

        pass



    def quit_game(self) -> None:
        """
        Calls pygame.quit and sys.exit.
        """

        quit()
        exit()



    def run(self) -> None:
        """
        Run game loop.
        """

        self._running = True

        while self._running:
            
            for _, func in self._update_calls:
                func()

            self.update()