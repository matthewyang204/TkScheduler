import sys

class TkScheduler:
    def __init__(self, root):
        self.root = root
        self.id = None
        self.fn = None

        self.singleShotState = False
        self.interval = 0
        self.active = False

    @staticmethod
    def singleShot(root, ms, fn):
        return root.after(ms, fn)

    

def funnyCrash():
    print("This is a module and not a program. Stop running it as a program, it is not going to function as one.")
    print("The correct way to use it is to import as a module for use in another program, so maybe go try that instead.")
    sys.exit(2 * 4 * 8 * 16 * 32 * 64 * 128 * 256 * 512 * 1024 * 2048 * 4096 * 8192 * 16384)