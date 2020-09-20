from calculator import Calculator
from loopTest import LoopTest

class OperatingSystem(object):

    def unknown(self):
        print("Unknown Command.")

    def hlp(self):
        print("List of Commands:")
        print("run - Runs an application.")
        print("printAll - Prints all arguments given, used for debugging.")
        print("shutdown - Shuts down the Operating System.")

    def run(self, args):
        prog = self.programs.get(args[0])
        newArgs = []
        for i in range(len(args)):
            if i == 0:
                continue
            newArgs.append(args[i])
        prog.link(newArgs)

    def printAll(self, args):
        print(args)

    def shutdown(self):
        self.isShutdown = True

    def __init__(self):
        self.isShutdown = False
        self.programs = {
            "Calculator": Calculator(),
            "LoopTest": LoopTest()
        }
        return

    def processCommand(self, cmd, args):
        if cmd == "help":
            self.hlp()
        elif cmd == "run":
            self.run(args)
        elif cmd == "printAll":
            self.printAll(args)
        elif cmd == "shutdown":
            self.shutdown()
        else:
            self.unknown()
        

    

print("JoshOS [PTOS]")
print("Python")
print("Testing")
print("Operating")
print("System")
print("")
print("")

OS = OperatingSystem()

while True:
    cmd = input("> ")

    cmdSpl = cmd.split(" ")

    cmdName = cmdSpl[0]
    args = []
    for i in range(len(cmdSpl)):
        if i == 0:
            continue
        args.append(cmdSpl[i])

    OS.processCommand(cmdName, args)

    if OS.isShutdown == True:
        break








