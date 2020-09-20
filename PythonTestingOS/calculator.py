import re

class Calculator:

    def __init__(self):
        return

    def link(self, args):

        if len(args) == 0:
            self.BeginCalculate()
            return

        if args[0] == "add":
            print(self.add(args[1], args[2]))
        elif args[0] == "sub":
            print(self.sub(args[1], args[2]))
        elif args[0] == "diff":
            print(self.diff(args[1], args[2]))
        elif args[0] == "mult":
            print(self.mult(args[1], args[2]))
        elif args[0] == "div":
            print(self.div(args[1], args[2]))

    def add(self, num1, num2):
        return float(num1) + float(num2)

    def sub(self, num1, num2):
        return float(num1) - float(num2)

    def diff(self, num1, num2):
        if float(num1) > float(num2):
            return float(num1) - float(num2)
        elif float(num2) > float(num1):
            return float(num2) - float(num1)
        else:
            return 0

    def mult(self, num1, num2):
        return float(num1) * float(num2)

    def div(self, num1, num2):
        return float(num1) / float(num2)

    def BeginCalculate(self):
        value = 0
        start = True
        inpt = ""

        while True:
            inpt = str(input("Enter operation (include spaces between operator and numbers) or 'stop' to end calculation: "))

            if inpt == "stop":
                break

            num1 = 0
            op = ""
            num2 = 0
            vals = re.split("\s", inpt)
        
            if (len(vals) > 2 and start == False) or len(vals) > 3 or len(vals) < 2:
                print("Error on input.")
                continue
        

            valstart = 1
            if start == False:
                valstart = 0
                num1 = value
            else:
                num1 = float(vals[0])
                start = False

            op = vals[valstart]
            num2 = float(vals[valstart + 1])

            if op == "+":
                value = num1 + num2
            elif op == "-":
                value = num1 - num2
            elif op == "*":
                value = num1 * num2
            elif op == "/":
                value = num1 / num2
        
            print(value)
