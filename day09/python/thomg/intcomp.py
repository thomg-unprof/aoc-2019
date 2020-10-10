import sys

class integerComputer:
    program = []
    inputs = []
    outputs = []
    pointer = 0
    revBase = 0
    
    def reset(self):
        self.program = []
        self.inputs = []
        self.outputs = []
        self.pointer = 0
        self.revBase = 0

    def readProgramFile(self, filename):
        """presume filename to be a absolute path"""
        with open(filename) as file:
            programString = file.readlines()
        self.program = programString[0].split(",")
        self.program = list(map(int, self.program))
    
    def addMemory(self, fields):
        self.program += ([0] * fields)

    def getArgument(self, pointer, mode):
        if mode == 0:
            return self.program[ self.program[ pointer ] ]
        if mode == 1:
            return self.program[ pointer ]
        if mode == 2:
            return self.program[ self.revBase + self.program[ pointer ] ]

    def add(self, mode1, mode2, mode3):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        sum = arg1 + arg2
        targetAddress = self.program[ self.pointer+3 ]
        if mode3 == 2:
            targetAddress += self.revBase
        self.program[ targetAddress ] = sum
        self.pointer += 4

    def multiply(self, mode1, mode2, mode3):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        product = arg1 * arg2
        targetAddress = self.program[ self.pointer+3 ]
        if mode3 == 2:
            targetAddress += self.revBase
        self.program[ targetAddress ] = product
        self.pointer += 4

    def input(self, inputValue, mode1):
        if mode1 != 2:
            targetAddress = self.program[ self.pointer+1 ]
        else:
            targetAddress = self.revBase + self.program[ self.pointer+1 ]
        self.program[ targetAddress ] = inputValue
        self.pointer += 2

    def output(self, mode1):
        outputValue = self.getArgument(self.pointer+1, mode1)
        print ("output at "+str(self.pointer)+": "+str(outputValue))
        self.pointer += 2
        self.outputs.append(outputValue)

    def jumpIfTrue(self, mode1, mode2):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        if arg1:
            self.pointer = arg2
        else:
            self.pointer +=3
    
    def jumpIfFalse(self, mode1, mode2):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        if not arg1:
            self.pointer = arg2
        else:
            self.pointer +=3
    
    def lessThan(self, mode1, mode2, mode3):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        address = self.program[ self.pointer+3 ]
        if mode3 == 2:
            address += self.revBase
        if arg1 < arg2:
            self.program[ address ] = 1
        else:
            self.program[ address ] = 0
        self.pointer += 4

    def equals(self, mode1, mode2, mode3):
        arg1 = self.getArgument(self.pointer+1, mode1)
        arg2 = self.getArgument(self.pointer+2, mode2)
        address = self.program[ self.pointer+3 ]
        if mode3 == 2:
            address += self.revBase
        if arg1 == arg2:
            self.program[ address ] = 1
        else:
            self.program[ address ] = 0
        self.pointer += 4

    def revBaseOffset(self, mode1):
        arg1 = self.getArgument(self.pointer+1, mode1)
        self.revBase += arg1
        self.pointer += 2

    def run(self, inputValue):
        self.pointer = 0
        counter = 0
        while 1:
            counter+=1
            instruction = self.program[ self.pointer ]
            opcode = instruction % 100
            instruction -= opcode
            mode1 = (instruction % 1000)   / 100
            instruction -= mode1*100
            mode2 = (instruction % 10000)  / 1000
            instruction -= mode2*1000
            # mode for the third parameter isn't actually needed on day05
            # all opcodes so far HAVE to be in position mode for their third param, if they have one
            mode3 = (instruction % 100000) / 10000

            if opcode == 1:
                self.add(mode1, mode2, mode3)
            
            elif opcode == 2:
                self.multiply(mode1, mode2, mode3)

            elif opcode == 3:
                self.input(inputValue, mode1)
            
            elif opcode == 4:
                self.output(mode1)

            elif opcode == 5:
                self.jumpIfTrue(mode1, mode2)

            elif opcode == 6:
                self.jumpIfFalse(mode1, mode2)
            
            elif opcode == 7:
                self.lessThan(mode1, mode2, mode3)

            elif opcode == 8:
                self.equals(mode1, mode2, mode3)

            elif opcode == 9:
                self.revBaseOffset(mode1)
            
            elif opcode == 99:
                break
            
            else:
                print(str(opcode)+"is not a correct opcode, terminating")
                break
        #print(str(self.program))
        return 0

intcomp = integerComputer()

# day 09
#intcomp.reset()
#intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day09.txt")
#intcomp.addMemory(10000)
#intcomp.run(1)


##########################################################################################
# day02
#intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day02.txt")
#intcomp.run(0)
#print ("day 02 star 1: "+str(intcomp.program[0]))

# day05
#intcomp.program=[]
#intcomp.pointer=0
#intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day05.txt")
# star 1
#intcomp.run(1)
# star 2
#intcomp.run(5)