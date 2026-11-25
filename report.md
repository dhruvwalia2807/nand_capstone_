# Project Report: Hack Computer Architecture and Assembler

## 1. Introduction
The project explores the relationship between assembly language, machine code and a simple computer architecture. It implements a two-pass assembler and provides HDL descriptions for the processor, memory subsystem and top-level computer.

## 2. Objectives
- Understand the Hack A-instruction and C-instruction formats.
- Build a symbol table for predefined symbols, labels and variables.
- Translate assembly mnemonics into 16-bit binary instructions.
- Study the CPU datapath, control signals, memory map and program counter.
- Validate the assembler with automated tests.

## 3. System Design
The assembler uses two passes. During pass one, labels are mapped to ROM instruction addresses. During pass two, instructions are encoded and unresolved symbols are assigned RAM addresses beginning at 16. The HDL folder separates CPU, Memory and Computer designs.

## 4. Implementation
The Python program uses lookup tables for computation, destination and jump fields. It strips comments and whitespace, checks symbols and numeric bounds, and reports errors with source line numbers. Sample programs demonstrate arithmetic, comparison, loops and screen memory access.

## 5. Testing
The unit test suite checks basic instruction translation, label and variable allocation, predefined symbols, invalid mnemonics and out-of-range constants. Run it with `python -m unittest discover -s tests -v`.

## 6. Result
The assembler generates one 16-bit binary word for each valid assembly instruction. The generated `.hack` files can be loaded into the Nand2Tetris CPU Emulator. HDL simulation should be run in the Hardware Simulator to verify chip behavior.

## 7. Conclusion
This project provides practical experience with instruction encoding, symbol resolution and the organization of a simple von Neumann-style computer. Further work could add richer diagnostics, assembler listing files and additional CPU integration tests.
