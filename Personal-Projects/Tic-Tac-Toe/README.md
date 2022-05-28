# Tic-Tac-Toe

## Summary 
This Python script simulates Tic-Tac-Toe. 

The Player plays against the CPU.

The Player can select which character they want to use, X or O, and the CPU will be assigned the character the Player does not choose. 

The Player can select the difficulty of the CPU. 

The Board is updated after each turn and is outputted to the user. 

The game ends in the following two ways: 
* When the Player or CPU achieves three in a row and a winner is declared
* If all the positions on the board are filled with neither the Player nor the CPU achieving three in a row, it is ruled as a Cat's Game 

When the game ends, the Player is prompted to play again or quit. 




## Background
This script was inspired by a mini exercise from Automate The Boring Stuff with Python. 
The setup was shown in the course as an example for dictionaries and their helpful use cases. 
It assigned the keys in the dictionary to the corresponding the position on the tic-tac-toe board:  
* top-L, top-M, top-R: top row right column, top row middle column, top row left column
* mid-L, mid-M, mid-R: mid row right column, mid row middle column, mid row left column
* low-L, low-M, low-R: low row right column, low row middle column, low row left column

And the values in the dictionary would represent what character occupied that space: X, O, or empty 

Our dictionary structure represented the following board: 

 top-L | top-M | top-R 
 
\-----------------------
 
 mid-L | mid-M | mid-R 
 
\-----------------------
 
 low-L | low-M | low-R 

I implemented all features given this foundation and all solutions after this were entirely developed on my own.   
