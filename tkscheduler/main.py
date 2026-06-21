import sys

class TkScheduler:
    def __init__(self, root):
        self.root = root
        self.id = None
        self.fn = None
        self.selfScheduleId = None

        self.singleShotState = False
        self.interval = 0

    @staticmethod
    def singleShot(root, ms, fn):
        return root.after(ms, fn)

    def isActive(self):

    def stop(self):
        if self.id != None or self.selfScheduleId != None:
            self.root.after_cancel(self.id)
            self.root.after_cancel(self.selfScheduleId)
            self.id = None
            self.selfScheduleId = None
        else:
            print("WARNING: Job already cancelled or not started yet")

    def start(self, ms):
        if self.id != None:
            print("WARNING: Not starting new job, job already in progress")
            return

        self.id = self.root.after(ms, self.fn)
        self.selfScheduleId = self.root.after(ms, lambda: self.start(ms))

def funnyCrash():
    print("This is a module and not a program. Stop running it as a program, it is not going to function as one.")
    print("The correct way to use it is to import as a module for use in another program, so maybe go try that instead.")
    sys.exit(2 * 4 * 8 * 16 * 32 * 64 * 128 * 256 * 512 * 1024 * 2048 * 4096 * 8192 * 16384)