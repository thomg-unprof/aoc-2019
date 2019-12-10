class IntcodeComputer:
    def __init__(self, filename, verbose = 1):
        with open(filename) as file:
            self.program = file.readlines()[0]
        self.program = self.program.split(",")
        self.program = list(map(int, self.program))
        self.program += ([0] * 10000)
        self.verbose = verbose
        self.pointer = 0    
        self.base = 0
        self.input = []
        self.output = 0
        self.has_terminated = 0

    def parseInstruction(self, instruction):
        opcode = instruction % 100
        modes = [int(instruction/100) % 10, int(instruction/1000) % 10, int(instruction/10000) % 10]
        return (opcode, modes)
    
    def getArgument(self, mode, offset, write = 0):
        if mode == 0:
            if not write:
                return self.program[self.program[self.pointer+offset]]
            else:
                return self.program[self.pointer+offset]
        if mode == 1:
            if not write:
                return self.program[self.pointer+offset]
            else: # this should never occur, I think? the spec is unclear
                return self.pointer+offset
        if mode == 2:
            if not write:
                return self.program[self.program[self.pointer+offset]+self.base]
            else:
                return self.program[self.pointer+offset]+self.base

    def run(self):
        val = -1
        while val < 0:
            (opcode, modes) = self.parseInstruction(self.program[self.pointer])
            val = self.executeInstruction(opcode, modes)
        return val
        
    def executeInstruction(self, opcode, modes):
        if opcode == 1: # add
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            arg3 = self.getArgument(modes[2], 3, 1)
            self.program[arg3] = arg1+arg2
            self.pointer += 4
        elif opcode == 2: # multiply
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            arg3 = self.getArgument(modes[2], 3, 1)
            self.program[arg3] = arg1*arg2
            self.pointer += 4
        elif opcode == 3: # input
            if not len(self.input):
               return 2
            arg1 = self.getArgument(modes[0], 1, 1)
            self.program[arg1] = self.input[0]
            self.input.pop(0)
            self.pointer += 2
        elif opcode == 4: # output
            arg1 = self.getArgument(modes[0], 1)
            self.output = self.program[arg1]
            if self.verbose:
                print("output at {}: {}".format(self.pointer, self.output))
            self.pointer += 2
        elif opcode == 5: # jump if true
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            self.pointer = arg2 if arg1 else self.pointer+3
        elif opcode == 6: # jump if false
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            self.pointer = arg2 if not arg1 else self.pointer+3
        elif opcode == 7: # less than
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            arg3 = self.getArgument(modes[2], 3, 1)
            self.program[arg3] = 1 if arg1 < arg2 else 0
            self.pointer += 4
        elif opcode == 8: # equals
            arg1 = self.getArgument(modes[0], 1)
            arg2 = self.getArgument(modes[1], 2)
            arg3 = self.getArgument(modes[2], 3, 1)
            self.program[arg3] = 1 if arg1 == arg2 else 0
            self.pointer += 4
        elif opcode == 9: # adjust base
            arg1 = self.getArgument(modes[0], 1)
            self.base += arg1
            self.pointer += 2
            print(self.program[1000])
        elif opcode == 99: # terminate
            self.has_terminated = 1
            return 0
        else:
            return 2
        return -1
            