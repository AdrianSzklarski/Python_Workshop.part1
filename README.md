*** Guess the number [in progress]: ***

0. the user declares the range of numbers to play;
1. the user is to declare whether he or the computer is guessing
1a. If the computer is playing, the user has to declare the number;
1b. Within 10 moves, the user tells the computer whether it has drawn too many or too few;
2a. If the user plays the message "too many", "too few", "you won", "the number given is out of range" appears;
3. in each case the program is to handle possible game errors;
4. the game is to be implemented in Flash;





*** Dice [in progress]: *** 

Board games and paper RPGs use many types of dice, not just the well-known cubic ones. One of the more popular dice, for example, is the ten-wall dice, or even the hundred-wall dice! Since dice are thrown frequently in games, it would be tedious, difficult and waste a lot of paper to write every time e.g. "throw two dice of ten walls and add 20 to the result". In such situations the code "throw 2D10+20" is used.

The code of such a cube looks as follows: xDy+z, where:

y - the type of dice to be used (e.g. D6, D10),
x - number of dice throws; if we throw once, this parameter is negligible,
z - the number to add (or subtract) to the result of the throws (optional).

Examples:

2D10+10: 2 throws of D10, add 10 to the result,
D6: an ordinary throw of a cube,
2D3: a toss of two three sided dice,
D12-1: a throw of D12 dice, subtract 1 from the result.

Write a function that:
 
accepts such a code in a string as a parameter,
recognises all input data:
type of dice,
number of throws,
modifier,
if the given string is invalid, it will return an appropriate message,
simulates the throws and returns the result.
Types of dice used in games: D3, D4, D6, D8, D10, D12, D20, D100;





*** Lotto [in progress]: ***

Big Dart, Small Dart and Mulilot Simulator:

Write a program that:

queries for typed numbers, while checking the following conditions:
whether the entered string is a valid number,
whether the user has not entered this number before,
whether the number belongs to the range 1-46, 1-49, 1-80;
after entering a sufficient number of numbers, it will sort them in ascending order and display them on the screen,
draws numbers from the range and displays them on the screen,
it will inform the player how many numbers he got;





*** Game 2001 [in progress]: ***

Implement the game 2001, you will find the rules below.

2001 - Rules of the Game
Each player starts with 0 points.
In his turn, a player rolls 2 dice (standard hex dice).
The number of eyes thrown is added to the total number of points.
Starting on the second turn:
if the player throws a 7, he divides his number of points by this value discarding the fractional part,
if he throws 11, he multiplies his current number of points by this value.
The player who first reaches 2001 points wins.

Implementation
Implement the game in a version for two players.
Let it be a console application.
Let the second player be a computer.
After each round, display the current number of points.
The player's throw should take place when the user presses enter. The computer's throw occurs automatically, after the player's throw. Terminate the program when either the player or the computer reaches more than 2001 points.

Modification 1
You may have noticed that the current version of the game is not very interactive and is just about clicking the enter key. Let's try to make it a little more interactive.

Before each throw, give the player a choice.
Let him choose 2 dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.
The dice can be repeated, or the player can use 2 different dice.
Let the dice be selected by the player entering the appropriate string (one for each dice).
You can use the code from the Dice task.
Let the computer's choice of dice be random.
The rest of the rules remain the same.

Modification 2
Now try transferring your game to the server using Flask. To store information between turns, use hidden form fields. This is not the best solution (it can be prone to cheating), but we don't worry about it for now. Dice selection before the throw, should be done using the form.

