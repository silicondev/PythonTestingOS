class NameWriter:

	def __init__(self):
		pass

	def nameMethod(self):
		name = input("Please input your name: ")
		print("Hello " + name)

	def link(self, args):
		self.nameMethod()

	def run(self):
		self.nameMethod()

if __name__ == "__main__":
	nameWrite = NameWriter()
	nameWrite.run()