
import time



class Stopwatch:

    def __init__(self, start_immediately:bool=False):
        
        self._start_time = None
        self._elapsed_pause = 0
        self._time_paused = None
        self._running = False
        self._paused = False

        self._laps = []

        if start_immediately:
            self.start()



    def start(self, initial_offset:float=0) -> None:

        if self._running:
            raise RuntimeError("Stopwatch cannot be started while running. use reset()")
        if self._paused:
            raise RuntimeError("Stopwatch cannot be started while paused. use resume()")

        self._start_time = time.time() - initial_offset
        self._elapsed_pause = 0
        self._time_paused = None
        self._running = True
        self._paused = False

        self._laps = []

    

    def stop(self, return_elapsed:bool=True) -> None | float:

        if not self._running:
            raise RuntimeError("Stopwatch cannot be stopped while stopped. use reset()")

        if return_elapsed:
            elapsed = self.get_time_elapsed()
        else:
            elapsed = None
        
        self._running = False
        self._paused = False
        self._start_time = None
        self._time_paused = None
        self._elapsed_pause = 0

        self._laps = []

        return elapsed
    

    def resume(self) -> None:

        if not self._paused:
            raise RuntimeError("Stopwatch cannot be resumed while running.")
        
        
        if self._paused:
            pause_duration = time.time() - self._time_paused
            self._elapsed_pause += pause_duration
            self._paused = False
            self._time_paused = None



    def pause(self, return_elapsed:bool=True) -> None:

        if self._paused:
            raise RuntimeError("Stopwatch cannot be pasued while paused.")
        
        if self._running and not self._paused:
            self._time_paused = time.time()
            self._paused = True

        if return_elapsed:
            return self.get_time_elapsed()
        
    

    def reset(self, start_immediately:bool = False) -> None:

        self._start_time = time.time() if start_immediately else None
        self._elapsed_pause = 0
        self._time_paused = None
        self._running = start_immediately
        self._paused = False

        self._laps = []
        
    

    def lap(self) -> float:

        lap_time = self.get_time_elapsed()
        self._laps.append(lap_time)

        return lap_time
    


    def get_laps(self) -> list:

        return self._laps[:]
    


    def get_lap_durations(self) -> list:

        durations = []
        last = 0.0

        for lap in self._laps:
            durations.append(lap - last)
            last = lap
        
        return durations
    


    def get_time_elapsed(self) -> float:

        if self._start_time is None:
            return 0.0

        if self._paused:
            return self._time_paused - self._start_time - self._elapsed_pause
        elif self._running:
            return time.time() - self._start_time - self._elapsed_pause
        else:
            return 0.0
    


    def is_paused(self):

        return self._paused
    


    def is_running(self):

        return self._running
        
    

    def __str__(self) -> str:
        
        return f"{self.get_time_elapsed():.3f}s elapsed"
    


    def __repr__(self) -> str:

        return f"<Stopwatch running={self._running} paused={self._paused} elapsed={self.get_time_elapsed():.3f}s>"






class StopwatchManager:

    def __init__(self):
        
        self._stopwatches = {}
    


    def create_new_stopwatch(self, stopwatch_id:str, start_immediately:bool=False) -> None:

        if stopwatch_id not in self._stopwatches.keys():
            self._stopwatches[stopwatch_id] = Stopwatch(start_immediately)

        

    def delete_stopwatch(self, stopwatch_id:str) -> None:

        if stopwatch_id in self._stopwatches.keys():
            del self._stopwatches[stopwatch_id]
    


    @property
    def stopwatches(self) -> dict [str, Stopwatch]:

        return self._stopwatches



    def exists(self, stopwatch_id:str) -> bool:

        return stopwatch_id in self._stopwatches



    def get_stopwatch(self, stopwatch_id:str) -> Stopwatch:

        return self._stopwatches.get(stopwatch_id)
    


    def reset_all(self, start_immediately:bool = False) -> None:

        for sw in self._stopwatches.values():
            sw.reset(start_immediately)



    def start_all(self, initial_offset:float = 0.0) -> None:

        for sw in self._stopwatches.values():
            sw.start(initial_offset)

    

    def stop_all(self, return_elapsed: bool = False) -> dict[str, float | None]:
        
        return {stopwatch_id: stopwatch.stop(return_elapsed) for stopwatch_id, stopwatch in self._stopwatches.items()}



    def pause_all(self) -> None:

        for sw in self._stopwatches.values():
            sw.pause(return_elapsed=False)



    def resume_all(self) -> None:

        for sw in self._stopwatches.values():
            sw.resume()
    


    def get_all_paused(self) -> dict[str, Stopwatch]:

        return {stopwatch_id: stopwatch for stopwatch_id, stopwatch in self._stopwatches.items() if stopwatch.is_paused()}
    


    def is_paused(self, stopwatch_id:str) -> bool:

        stopwatch = self.get_stopwatch(stopwatch_id)

        return stopwatch.is_paused()
    


    def get_all_running(self) -> dict[str, Stopwatch]:

        return {stopwatch_id: stopwatch for stopwatch_id, stopwatch in self._stopwatches.items() if stopwatch.is_running()}
    


    def is_running(self, stopwatch_id:str) -> bool:

        stopwatch = self.get_stopwatch(stopwatch_id)

        return stopwatch.is_running()
    


    def get_time_elapsed(self, stopwatch_id:str) -> float:

        stopwatch = self.get_stopwatch(stopwatch_id)

        return stopwatch.get_time_elapsed()



    def get_laps(self, stopwatch_id:str) -> list:

        stopwatch = self.get_stopwatch(stopwatch_id)

        return stopwatch.get_laps()
    


    def get_lap_durations(self, stopwatch_id:str) -> list:

        stopwatch = self.get_stopwatch(stopwatch_id)

        return stopwatch.get_lap_durations()
    


    def __contains__(self, stopwatch_id:str) -> bool:

        return stopwatch_id in self._stopwatches



    def __len__(self) -> int:

        return len(self._stopwatches)
    


    def __repr__(self):

        return f"<StopwatchManager count={len(self)} running={len(self.get_all_running())}>"