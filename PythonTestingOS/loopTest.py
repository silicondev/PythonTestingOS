import sys

class LoopTest:

    def __init__(self, maxInt, maxSqr): # Added option to add these numbers on init
        self.maxInt = maxInt
        self.maxSqr = maxSqr

    def __init__(self):
        return

    def startCount(self):
        for i in range(self.maxInt):
            if i == 0: # Skipping 0 as spec needed 1 - 100, not 0 - 100
                continue

            sqr = i ** 2
            if (sqr >= self.maxSqr):
                break
            print(str(i) + " - " + str(sqr))

    def link(self, args): # This is used in a basic 'Python Testing Operating System (PTOS)' I have written to house any of these small projects from one runnable command line. This can be ignored.
        self.run()

    def run(self): # This is the real run method.
        self.maxInt = int(input("Please enter the maximum non-squared number: "))
        self.maxSqr = float(input("Please enter the maximum squared number: "))
        self.startCount()

# Running code
if __name__ == "__main__":
    test = LoopTest()
    test.run()