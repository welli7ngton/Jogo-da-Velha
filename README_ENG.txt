# Tictactoe
 Repository for project 1 of Cisco's Python course.

                                    Tic-tac-toe PROJECT
Scenario
Your task is to write a simple program that pretends to play tic-tac-toe with the user. To make everything easier for you, we decided to simplify the game. Here are our assumptions:

the computer ( your program) must play using 'X's;
the user (you) must play using 'O's;

the first move belongs to the computer - it always places its first 'X' in the middle of the frame; all squares are numbered row by row, starting with 1


the user enters his move by entering the number of the chosen square - the number must be valid, that is, it must be an integer, must be greater than 0 and less than 10, and cannot point to a field that is already occupied;

the program checks if the game is over - there are four possible verdicts: the game must continue, the game ends in a draw, you win or the computer wins;

the computer responds to your movement and the check is repeated;

do not implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.


Requirements
Implement the following features:

the panel must be stored as a list of three elements, while each element is another list of three elements (the
winner lists represent lines) so that all squares can be accessed using the following syntax:


    board[row][col]


each of the elements of the internal list can contain "O", "X" or a digit representing the number of the square 
(such square is considered free)

the appearance of the frame should be exactly as shown in the example.
implement the functions defined for you in the editor.