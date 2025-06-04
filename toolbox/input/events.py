
import pygame



def get_events():
    """
    Returns a list of all active events.
    """
    return pygame.event.get()



def is_event(pygame_event:pygame.event):
    """
    Returns True if passed event is active, else False.

    pygame_event : the pygame.event to check for
    """

    for event in get_events():
        if event.type == pygame_event:
            return True
        
    return False



def handle_event(pygame_event:pygame.event, callback:callable):
    """
    Calls a callback if the passed event is active.

    pygame_event : the pygame.event to check for
    callback : the callable to callback
    """

    for event in get_events():
        if event.type == pygame_event:
            callback()