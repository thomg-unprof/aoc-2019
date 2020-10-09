import pytest

from intcomp_refactor import integerComputer

@pytest.fixture
def intcomp():
    """intcomp with empty program"""
    return integerComputer()



def test_readProgramFile(intcomp):
    intcomp.readProgramFile("testfile.txt")
    assert intcomp.program == [1,2,3,4,7]

def test_getArgument(intcomp):
    intcomp.program = [1,4,5,6,35,12,0]
    assert intcomp.getArgument(1, 0) == 35
    assert intcomp.getArgument(1, 1) == 4

def test_add(intcomp):
    intcomp.program = [1,4,5,6,35,12,0]
    intcomp.add(0, 0)
    assert intcomp.program == [1,4,5,6,35,12,47]
    assert intcomp.pointer == 4

def test_multiply(intcomp):
    intcomp.program = [1,4,5,6,6,12,0]
    intcomp.multiply(0, 0)
    assert intcomp.program == [1,4,5,6,6,12,72]
    assert intcomp.pointer == 4

def test_input(intcomp):
    intcomp.program = [3, 2, 0]
    intcomp.input(17)
    assert intcomp.program == [3, 2, 17]
    assert intcomp.pointer == 2

def test_output(intcomp):
    intcomp.program = [4, 2, 0]
    assert intcomp.output(0) == 0
    intcomp.pointer = 0
    assert intcomp.output(1) == 2
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
    intcomp.lessThan(1,1)
    assert intcomp.program == [1, 0, 2, 0]
    intcomp.pointer = 0
    intcomp.program = [6, 0, 2, 0]
    intcomp.lessThan(0,1)
    assert intcomp.program == [0, 0, 2, 0]
    assert intcomp.pointer == 4

def test_equals(intcomp):
    intcomp.program = [7, 0, 2, 0]
    intcomp.equals(1,1)
    assert intcomp.program == [0, 0, 2, 0]
    intcomp.pointer = 0
    intcomp.program = [7, 1, 1, 0]
    intcomp.equals(0,1)
    assert intcomp.program == [1, 1, 1, 0]
    assert intcomp.pointer == 4