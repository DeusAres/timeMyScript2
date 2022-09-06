import time

class timer:
    def __init__(self):
        self.strt = None
        self.end = None
        self.pauseStart = 0
        self.pauseEnd = 0
        self.totalPause = 0
        self.mark = 0
        self.running = False
        self.paused = False

    def start(self):
        if not self.running:
            self.strt = time.time()
            self.mark = self.strt
            self.running = True
            print(f"TimeMyScript2 (START): Started")
        else:
            print(f"TimeMyScript2 (START): Already running")


    def stop(self):
        if  self.running:
            self.end = time.time()
            self.running = False
            self.resetPause()
            print(f"TimeMyScript2 (STOPPED): {self.end - self.strt - self.pauseDiff()} s")
        else:
            print(f"TimeMyScript2 (START): Already stopped")

    def pause(self):
        if not self.paused and self.running:
            self.pauseStart = time.time()
            self.paused = True
            print(f"TimeMyScript2 (PAUSE): Paused at {str(time.time()-self.strt)[:5]} s")
        elif not self.running:
            print(f"TimeMyScript2 (PAUSE): Can't pause not running timer")
        elif self.paused:
            print(f"TimeMyScript2 (PAUSE): Already paused")

    def resume(self):
        if self.paused:
            a = time.time()
            self.totalPause += a - self.pauseStart
            self.pauseEnd = a
            print(f"TimeMyScript2 (RESUME): Resumed at {str(time.time()-self.strt - self.pauseDiff())[:5]} s")
            self.resetPause()
        elif not self.paused and self.running:
            print(f"TimeMyScript2 (RESUME): Already running")
        else:
            print(f"TimeMyScript2 (RESUME): Can't resume stopped timer")

    def pauseDiff(self):
        if not self.pauseEnd:
            self.pauseEnd = time.time()
        return self.pauseEnd - self.pauseStart

    def lap(self):
        if not self.running or self.paused:
            if not self.running : add = "not running" 
            if self.paused : add = "paused" 
            print("TimeMyScript2 (LAP): Can't lap while " + add)
        else:
            print(f"TimeMyScript2 (LAP):  [LAP - {str(time.time() - self.mark )[:5]}s] | [TOTAL - {str(time.time()-self.strt - self.pauseDiff())[:5]} s]")
            self.mark = time.time()

    def resetPause(self):
        self.pauseEnd = 0
        self.pauseStart = 0
        self.paused = False
t = timer()
