import sys

class integerComputer:
    program = []


    def readProgramFile(self, filename):
        """presume filename to be a relative path"""
        with open(filename) as file:
            programString = file.readlines()
        self.program = programString[0].split(",")
        self.program = list(map(int, self.program))

    def run(self):
        return 0

