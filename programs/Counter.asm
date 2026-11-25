// Simple loop: increment RAM[10] five times
@R10
M=0
@5
D=A
@COUNT
M=D
(LOOP)
@R10
M=M+1
@COUNT
MD=M-1
@LOOP
D;JGT
(END)
@END
0;JMP
