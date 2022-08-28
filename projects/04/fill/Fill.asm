// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
@8191 // number of screen address blocks
M=A
@SCREEN
D=A
@address
M=D
@KBD
D=M
@FILL
D;JNE
@UNFILL
D;JEQ
(FILL)
@address
A=M
M=-1
@address
M=M+1
A=M
M=-1
@8191
MD=M-1
@END
D;JEQ
@FILL
0;JMP
(UNFILL)
@address
A=M
M=0
@address
M=M+1
@8191
MD=M-1
@END
D;JLT
@UNFILL
D=M
0;JMP


(END)
@LOOP
0;JMP




