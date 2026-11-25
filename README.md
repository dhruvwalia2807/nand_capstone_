# Hack Computer Capstone — Assembler and Architecture

## Overview
This project is an independent implementation of a two-pass assembler for the 16-bit Hack instruction set, accompanied by HDL design files for the CPU, memory map and complete computer.

## Folder structure
- `assembler.py` — translates Hack assembly into 16-bit machine instructions.
- `programs/` — small assembly programs for arithmetic, comparison, counting and screen memory.
- `hdl/` — CPU, Memory and Computer HDL source files.
- `tests/` — automated checks for instruction encoding, symbols and invalid input.
- `output/` — generated `.hack` files.

## Requirements
- Python 3.9 or newer
- Nand2Tetris Software Suite (only needed to load and simulate HDL files)

## Run the assembler
From this folder:
```bash
python assembler.py programs/Add.asm
```
Choose an output filename:
```bash
python assembler.py programs/Max.asm output/Max.hack
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Two-pass approach
1. The first pass removes comments and whitespace, records label addresses, and counts instruction positions.
2. The second pass converts A-instructions and C-instructions to 16-bit binary words. New variables are allocated from RAM address 16.

## Instruction format
- A-instruction: `0vvvvvvvvvvvvvvv`
- C-instruction: `111accccccdddjjj`

The assembler validates symbols, numeric range, computation mnemonics, destination fields and jump fields. On invalid input it reports the source line.

## HDL simulation
Open the Nand2Tetris Hardware Simulator, load the HDL files from `hdl/`, and test the chips against the supplied course `.tst` scripts / built-in chip tests. These HDL files are source designs; successful simulation must be verified in the simulator.

## Academic note
This is a learning implementation. Review the code, run the tests, and be prepared to explain the assembler passes, symbol table, instruction fields and CPU datapath.
