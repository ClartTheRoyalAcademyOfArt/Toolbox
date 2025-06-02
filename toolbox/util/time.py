
import time





class TimeoutTimer:

    def __init__(self, duration:float, callback:callable=None, start_immediately:bool=False):
        
        self.duration = duration
        self.callback = callback

        self._timedout = False

        self._active = False
        self._start_time = None
        self._time_paused = None
        self._time_elapsed = 0
        
        if start_immediately:
            self.start()
    


    def start(self):
        """
        Starts timer from zero
        """

        if self._timedout:
            raise RuntimeError("Timer cannot be started while timedout. Use reset()")
        if self._time_paused is not None:
            raise RuntimeError("Timer cannot be started while paused. Use resume()")

        if not self._active:
            self._active = True
            self._start_time = time.time()
    


    def stop(self, timeout:bool=False):
        """
        Stops running timer, resets values, sets self._active to False

        timeout : if True, calls self.timeout()
        """

        if self._timedout:
            raise RuntimeError("Timer cannot be stopped while timedout. Use reset()")
        
        if timeout:
            self.timeout()

        self._active = False
        self._start_time = None
        self._time_paused = None
        self._time_elapsed = 0

    

    def pause(self):
        """
        Pauses running timer, sets self._active to False.
        """

        if self._timedout:
            raise RuntimeError("Timer cannot be paused while timedout.")
        if self._time_paused is not None:
            raise RuntimeError("Timer cannot be paused while paused. Use resume()")

        self._active = False
        self._time_paused = time.time()
    

    
    def resume(self):
        """
        Resumes paused timer.
        """

        if self._timedout:
            raise RuntimeError("Timer cannot be resumed while timedout. Use reset()")

        if self._time_paused is not None:
            self._active = True
            self._start_time += (time.time() - self._time_paused)
            self._time_paused = None
        
    

    def reset(self, start_immediately:bool=False):
        """
        Reset timer to zero.

        start_immediately : if True, timer starts immediately
        """

        self._active = start_immediately
       
        self._start_time = time.time() if start_immediately else None

        self._timedout = False
        self._time_paused = None
        self._time_elapsed = 0
    


    def time_elapsed(self):
        """
        Returns elapsed time.
        """

        return self._time_elapsed
    


    def active(self):
        """
        Returns True if active.
        """

        return self._active



    def timedout(self):
        """
        Returns if timedout.
        """

        return self._timedout


    
    def tick(self):
        """
        Ticks timer, timesout if duration is exceeded.
        """

        if self._active:
            current = time.time()
            self._time_elapsed = current - self._start_time

            if self._time_elapsed >= self.duration:
                self.timeout()
    


    def timeout(self):
        """
        Timesout timer.
        """

        self._timedout = True

        self._active = False
        self._start_time = None
        self._time_paused = None
        self._time_elapsed = 0

        if self.callback is not None:
            self.callback()
    


    def __repr__(self):

        return (f"<TimeoutTimer active={self._active} timedout={self._timedout} "
                f"time_elapsed={self._time_elapsed:.2f}/{self.duration}>")

    

        





class TimerManager:

    def __init__(self):
        
        self._timers = {}
    


    def create_timer(self, timer_id:str, duration:float, callback:callable=None, start_immediately:bool=False):
        """
        Creates new timer.

        timer_id : string id for new timer
        duration : duration in seconds for new timer
        callback : optional callback on timeout
        start_immediately : if True, starts new timer immediately
        """

        if timer_id not in self._timers.keys():
            self._timers[timer_id] = TimeoutTimer(duration, callback, start_immediately)
        
    

    def delete_timer(self, timer_id:str):
        """
        Delete a timer.

        timer_id : timer to delete
        """

        if timer_id in self._timers.keys():
            del self._timers[timer_id]
    

    
    def tick_all(self):
        """
        Ticks all timers.
        """

        for timers in self._timers.values():

            timers.tick()
    


    @property
    def timers(self):
        """
        Timer dictionary
        """

        return self._timers
    


    def exists(self, timer_id:str):
        """
        Returns True if timer exists.

        timer_id : timer to check
        """

        return timer_id in self._timers
    


    def get_timer(self, timer_id:str):
        """
        Return a timer's object.

        timer_id : timer to return
        """

        return self._timers.get(timer_id)
    


    def get_all_active(self):
        """
        Returns all active timers.
        """

        return {timer_id: t for timer_id, t in self._timers.items() if t.active()}
    
    

    def is_active(self, timer_id:str):
        """
        Returns True if specified timer is active.

        timer_id : timer to check
        """

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.active()
    


    def get_time_elapsed(self, timer_id:str):
        """
        Get time elapsed for specified timer.

        timer_id : timer's elapsed time to get
        """

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.time_elapsed()



    def is_timedout(self, timer_id:str):
        """
        Returns True if specified timer is timedout.

        timer_id : timer to check
        """

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.timedout()
    


    def __contains__(self, timer_id: str):

        return timer_id in self._timers



    def __len__(self):
        return len(self._timers)