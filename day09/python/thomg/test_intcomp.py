import pytest

from intcomp_refactor import integerComputer

@pytest.fixture
def intcomp():
    """intcomp with empty program"""
    return integerComputer()



def test_readProgramFile(intcomp):
    intcomp.readProgramFile("testfile.txt")
    assert intcomp.program == [1,2,3,4,7]

def test_add(intcomp):
    intcomp.program = [1,4,5,6,35,12,0]
    intcomp.add()
    assert intcomp.program == [1,4,5,6,35,12,47]
    assert intcomp.pointer == 4

def test_multiply(intcomp):
    intcomp.program = [1,4,5,6,6,12,0]
    intcomp.multiply()
    assert intcomp.program == [1,4,5,6,6,12,72]
    assert intcomp.pointer == 4