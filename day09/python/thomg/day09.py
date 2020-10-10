from intcomp import integerComputer

intcomp = integerComputer()
intcomp.reset()

intcomp.readProgramFile("d:\\workspace\\aoc2019\\day09\\python\\thomg\\program_day09.txt")
intcomp.addMemory(10000)
intcomp.run(2)

#intcomp.program = [109, 1, 203, 2, 204, 2, 99]
#intcomp.run(42)

#[109, -1, 104, 1, 99] outputs 1
#[109, -1, 204, 1, 99] outputs 109
#[109, 1, 9, 2, 204, -6, 99] outputs 204
#[109, 1, 109, 9, 204, -6, 99] outputs 204
#[109, 1, 209, -1, 204, -106, 99] outputs 204
#[109, 1, 3, 3, 204, 2, 99] outputs the input
#[109, 1, 203, 2, 204, 2, 99] outputs the input