import pytest

from intcomp import integerComputer

@pytest.fixture
def intcomp():
    """intcomp with empty program"""
    intcomp = integerComputer()
    intcomp.program = []
    intcomp.outputs = []
    intcomp.intputs = []
    return intcomp



def test_readProgramFile(intcomp):
    intcomp.readProgramFile("testfile.txt")
    testprogram = [1,2,3,4,7]
    assert intcomp.program == testprogram

def test_addMemory(intcomp):
    intcomp.program = [0]
    intcomp.addMemory(1204978)
    assert intcomp.program == ([0] * 1204979)

def test_getArgument(intcomp):
    intcomp.program = [1,4,5,6,35,12,0]
    assert intcomp.getArgument(1, 0) == 35
    assert intcomp.getArgument(1, 1) == 4
    intcomp.revBase = 2
    assert intcomp.getArgument(1, 2) == 0

def test_add(intcomp):
    intcomp.program = [1,4,5,6,35,12,0]
    intcomp.add(0, 0, 2)
    assert intcomp.program == [1,4,5,6,35,12,47]
    assert intcomp.pointer == 4

def test_multiply(intcomp):
    intcomp.program = [1,4,5,6,6,12,0]
    intcomp.multiply(0, 0, 2)
    assert intcomp.program == [1,4,5,6,6,12,72]
    assert intcomp.pointer == 4

def test_input(intcomp):
    intcomp.program = [3, 2, 0]
    intcomp.input(17, 1)
    assert intcomp.program == [3, 2, 17]
    assert intcomp.pointer == 2

def test_output(intcomp):
    intcomp.program = [4, 2, 0]
    intcomp.output(0)
    assert intcomp.outputs[0] == 0
    intcomp.pointer = 0
    intcomp.output(1)
    assert intcomp.outputs[1] == 2
    assert intcomp.pointer == 2

def test_jumpIfTrue(intcomp):
    intcomp.program = [5, 0, 0, 6, 6]
    intcomp.jumpIfTrue(1,0)
    assert intcomp.pointer == 3
    intcomp.pointer = 0
    intcomp.program = [5, 1, 0, 6, 6, 7]
    intcomp.jumpIfTrue(0, 1)
    assert intcomp.pointer == 0
    intcomp.pointer = 0
    intcomp.program = [5, 1, 0, 6, 6, 7]
    intcomp.jumpIfTrue(0, 0)
    assert intcomp.pointer == 5

def test_jumpIfFalse(intcomp):
    intcomp.program = [5, 0, 0, 6, 6]
    intcomp.jumpIfFalse(1,0)
    assert intcomp.pointer == 5
    intcomp.pointer = 0
    intcomp.program = [5, 1, 0, 6, 6, 7]
    intcomp.jumpIfFalse(0, 1)
    assert intcomp.pointer == 3
    intcomp.pointer = 0
    intcomp.program = [5, 3, 0, 0, 6, 7]
    intcomp.jumpIfFalse(0, 0)
    assert intcomp.pointer == 5

def test_lessThan(intcomp):
    intcomp.program = [6, 0, 2, 0]
    intcomp.lessThan(1,1,2)
    assert intcomp.program == [1, 0, 2, 0]
    intcomp.pointer = 0
    intcomp.program = [6, 0, 2, 0]
    intcomp.lessThan(0,1,0)
    assert intcomp.program == [0, 0, 2, 0]
    assert intcomp.pointer == 4

def test_equals(intcomp):
    intcomp.program = [7, 0, 2, 0]
    intcomp.equals(1,1,0)
    assert intcomp.program == [0, 0, 2, 0]
    intcomp.pointer = 0
    intcomp.program = [7, 1, 1, 0]
    intcomp.equals(0,1,2)
    assert intcomp.program == [1, 1, 1, 0]
    assert intcomp.pointer == 4

def trest_revBaseOffset(intcomp):
    intcomp.revBase = 0
    intcomp.program = [109, 2, 6, 4, 7]
    intcomp.pointer = 0
    intcomp.revBaseOffset(1)
    assert intcomp.revBase == 2
    intcomp.pointer = 0
    intcomp.revBaseOffset(2)
    assert intcomp.revBase == 6
    assert intcomp.pointer == 2

def test_day02(intcomp):
    intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day02.txt")
    intcomp.run(0)
    assert intcomp.program[0] == 4462686

def test_day05(intcomp):
    intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day05.txt")
    intcomp.run(5)
    assert intcomp.outputs[0] == 8805067

def test_day09(intcomp):
    intcomp.pointer = 0
    intcomp.revBase = 0
    intcomp.program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    intcomp.addMemory(100000)
    intcomp.run(0)
    assert intcomp.outputs == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

    intcomp.pointer = 0
    intcomp.revBase = 0
    intcomp.outputs = []
    intcomp.program = [1102,34915192,34915192,7,4,7,99,0]
    intcomp.addMemory(100000)
    intcomp.run(0)
    assert len(str(intcomp.outputs[0])) == 16

    intcomp.pointer = 0
    intcomp.revBase = 0
    intcomp.outputs = []
    intcomp.program = [104,1125899906842624,99]
    intcomp.run(0)
    assert intcomp.outputs[0] == 1125899906842624

    intcomp.reset()
    intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day09.txt")
    intcomp.addMemory(10000)
    intcomp.run(2)
    assert intcomp.outputs[0] == 69781
