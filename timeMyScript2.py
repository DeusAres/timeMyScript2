import time

class timer:
    def __init__(self):
        self.__strt = None
        self.__psd = None
        self.__mark = 0
        self.__running = False
        self.__paused = False

    def __toggleRun(self):
        self.__running = False if self.__running else True
    def __togglePause(self):
        self.__paused = False if self.__paused else True
        self.__toggleRun()
    def __reset(self):
        self.__paused = False
        self.__running = False
        self.__strt = 0

    def statusAndTime(self):
        if self.__strt == None:
            print(f"TimeMyScript2 (SHOW): Timer never started")
            return
        elif self.__paused:
            string = "paused"
        elif self.__running:
            string = "running"
        else:
            string = "STOPPED"
        print(f"TimeMyScript2 (SHOW): {self.retrieveCurrent()} s and {string}")

    def retrieveCurrent(self):
        if self.__paused:
            return self.__psd - self.__strt
        elif self.__running:
            return time.time() - self.__strt

    def start(self):
        """
        Start a time or resume it from a pause
        """
        if not self.__running:
            if self.__paused:
                self.__strt += time.time() - self.__psd
                self.__mark = self.__strt
                self.__togglePause()
                print(f"TimeMyScript2 (RESUME): Resumed at {str(time.time() - self.__strt)[:5]} s")
            else:
                self.__strt = time.time()
                self.__mark = self.__strt
                print(f"TimeMyScript2 (START): Started")
                self.__toggleRun()
        else:
            print(f"TimeMyScript2 (START): Already running")

    def pause(self):
        if not self.__paused:
            self.__psd = time.time() # CHANGE
            self.__togglePause()

            print(f"TimeMyScript2 (PAUSE): paused at {str(self.__psd - self.__strt)[:5]} s")

        elif not self.__running:
            print(f"TimeMyScript2 (PAUSE): Can't pause not running timer")

        elif self.__paused:
            print(f"TimeMyScript2 (PAUSE): Already paused")
        


    def lap(self):
        if not self.__running or self.__paused:
            if not self.__running : add = "not running" 
            if self.__paused : add = "paused" 
            print("TimeMyScript2 (LAP): Can't lap while " + add)
        else:
            print(f"TimeMyScript2 (LAP):  [LAP - {str(time.time() - self.__mark)[:5]}s] | [TOTAL - {str(time.time() - self.__strt)[:5]} s]")
            self.__mark = time.time()

    
    def stop(self):
        if self.__running:
            print(f"TimeMyScript2 (STOPPED): {time.time() - self.__strt} s")
            self.__reset()
        elif self.__paused:
            print(f"TimeMyScript2 (STOPPED): {self.__psd - self.__strt} s")
            self.__reset()
        else:
            print(f"TimeMyScript2 (START): Already stopped")
 
t = timer()
