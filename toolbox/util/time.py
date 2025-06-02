
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
        
        if self._timedout:
            raise RuntimeError("Timer cannot be started while timedout. Use reset()")
        if self._time_paused is not None:
            raise RuntimeError("Timer cannot be started while paused. Use resume()")

        if not self._active:
            self._active = True
            self._start_time = time.time()
    


    def stop(self, timeout:bool=False):

        if self._timedout:
            raise RuntimeError("Timer cannot be stopped while timedout. Use reset()")
        
        if timeout:
            self.timeout()

        self._active = False
        self._start_time = None
        self._time_paused = None
        self._time_elapsed = 0

    

    def pause(self):

        if self._timedout:
            raise RuntimeError("Timer cannot be paused while timedout.")
        if self._time_paused is not None:
            raise RuntimeError("Timer cannot be paused while paused. Use resume()")

        self._active = False
        self._time_paused = time.time()
    

    
    def resume(self):

        if self._timedout:
            raise RuntimeError("Timer cannot be resumed while timedout. Use reset()")

        if self._time_paused is not None:
            self._active = True
            self._start_time += (time.time() - self._time_paused)
            self._time_paused = None
        
    

    def reset(self, start_immediately:bool=False):

        self._active = start_immediately
       
        self._start_time = time.time() if start_immediately else None

        self._timedout = False
        self._time_paused = None
        self._time_elapsed = 0
    


    def time_elapsed(self):

        return self._time_elapsed
    


    def active(self):

        return self._active



    def timedout(self):

        return self._timedout


    
    def tick(self):

        if self._active:
            current = time.time()
            self._time_elapsed = current - self._start_time

            if self._time_elapsed >= self.duration:
                self.timeout()
    


    def timeout(self):
        
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

        if timer_id not in self._timers.keys():
            self._timers[timer_id] = TimeoutTimer(duration, callback, start_immediately)
        
    

    def delete_timer(self, timer_id:str):

        if timer_id in self._timers.keys():
            del self._timers[timer_id]
    

    
    def tick_all(self):

        for timers in self._timers.values():

            timers.tick()
    


    @property
    def timers(self):

        return self._timers
    


    def exists(self, timer_id:str):

        return timer_id in self._timers
    


    def get_timer(self, timer_id:str):

        return self._timers.get(timer_id)
    


    def get_all_active(self):

        return {timer_id: t for timer_id, t in self._timers.items() if t.active()}
    
    

    def is_active(self, timer_id:str):

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.active()
    


    def get_time_elapsed(self, timer_id:str):

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.time_elapsed()



    def is_timedout(self, timer_id:str):

        timer = self.get_timer(timer_id)

        if timer is None:
            raise ValueError(f"Timer '{timer_id}' not found")
        
        return timer.timedout()
    


    def __contains__(self, timer_id: str):

        return timer_id in self._timers



    def __len__(self):
        return len(self._timers)