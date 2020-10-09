import sys

class integerComputer:
    program = []
    pointer = 0


    def readProgramFile(self, filename):
        """presume filename to be a relative path"""
        with open(filename) as file:
            programString = file.readlines()
        self.program = programString[0].split(",")
        self.program = list(map(int, self.program))

    def add(self):
        arg1 = self.program[ self.program[ self.pointer+1 ] ]
        arg2 = self.program[ self.program[ self.pointer+2 ] ]
        sum = arg1 + arg2
        targetAddress = self.program[ self.pointer+3 ]
        self.program[ targetAddress ] = sum
        self.pointer += 4

    def multiply(self):
        arg1 = self.program[ self.program[ self.pointer+1 ] ]
        arg2 = self.program[ self.program[ self.pointer+2 ] ]
        product = arg1 * arg2
        targetAddress = self.program[ self.pointer+3 ]
        self.program[ targetAddress ] = product
        self.pointer += 4

    def run(self):
        while 1:
            instruction = self.program[ self.pointer ]
            opcode = instruction % 100
            #instruction -= opcode
            #mode1 = (instruction % 1000)   / 100
            #instruction -= mode1*100
            #mode2 = (instruction % 10000)  / 1000
            #instruction -= mode2*1000
            # mode for the third parameter isn't actually needed on day05
            # all opcodes so far HAVE to be in position mode for their third param, if they have one
            #mode3 = (instruction % 100000) / 10000
            modes = []

            if opcode == 1:
                self.add()
            
            elif opcode == 2:
                self.multiply()
            
            elif opcode == 99:
                break
        
        print(str(self.program))
        return 0

intcomp = integerComputer()
intcomp.readProgramFile("program_day02.txt")
intcomp.run()
