
from typing import Callable

import pygame



class EventManager:

    def __init__(self):
        
        self._events = []


    
    def poll(self) -> None:
        """
        Poll and cache all current events. Call once per frame.
        """

        self._events = pygame.event.get()



    def is_event(self, event_type:int):
        """
        Returns True if the specified event type is in the current frame's events.

        event_type : an int constant from pygame (e.g. pygame.QUIT)
        """

        return any(event.type == event_type for event in self._events)
    


    def handle_event(self, event_type:int, callback:Callable[[], None]) -> None:
        """
        Calls a callback (no-arg) if specified event type is in the current frame's events.

        event_type : an int constant from pygame (e.g. pygame.QUIT)
        callback : a callable to callback on an event hit.
        """

        for event in self._events:
            if event.type == event_type:
                callback()

    

    def handle_event_with(self, event_type:int, callback:Callable[[pygame.event.Event], None]) -> None:
        """
        Calls a callback if specified event type is in the current frame's events. Passes event_type to the callback.

        event_type : an int constant from pygame (e.g. pygame.QUIT)
        callback : a callable to callback on an event hit.
        """

        for event in self._events:
            if event.type == event_type:
                callback(event)
    


    def get(self) -> list[pygame.event.Event]:
        """
        Returns all events polled in the current frame.
        """

        return self._events