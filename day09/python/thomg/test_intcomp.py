import pytest

from intcomp_refactor import integerComputer

@pytest.fixture
def intcomp():
    return integerComputer()


def test_readProgramFile(intcomp):
    intcomp.readProgramFile("testfile.txt")
    assert intcomp.program == [1,2,3,4,7]

