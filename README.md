# TIC TAC TOE 

#### Video Demo:  https://www.youtube.com/watch?v=hpxajvYWxdE 

#### Description:

CS50x Final Project - Tkinter/Python based game of Tic Tac Toe  

This project is the classic game of Tic Tac Toe. I have primarily been learning Python in my spare time, so decided I wanted to code this game in Python using Tkinter as the games Graphical User Interface (GUI).  

For the interface I have created a main menu screen which has the game title, a brief how to play description and five possible options in the form of buttons. These are - person-to-person, person vs computer (Easy mode), person vs computer (Medium mode), person vs computer (Hard mode) and Exit game. When one of the game modes are selected the menu screen is destroyed and the game screen is created. 

At the top of the game window is the game title. Below that are two buttons, one to go back to the main menu and another to reset the game. Below this is a label that indicates who is currently playing. Or if there is a winner or draw the label will indicate this also. Next is a 3 x 3 grid of buttons where the game is played.  

I had initially planned to just create a basic person vs person version of the game, but as the project progressed, I decided I wanted to add a 'vs computer' element to the game. 

Once the person-to-person game was coded I then made a copy of this code and modified it so that the second players turn became the computers turn. I did this by importing the random module and simply picked a random board position each time the computer played. Although this made the game more interesting it was too easy as the human player to win. This version of the game later became 'Easy mode'.  

Having deciding the pick random game was too easy, I searched online to find other ways of making the computer player more 'intelligent'. This led me to discover the minimax algorithm. This was not straight forward to implement as initially minimax was set to make changes directly to the game board. When minimax was run it would instantly fill all the boxes and win the game in one turn. I later decided that minimax was to use a dictionary which kept track of all the played positions on the board. It could then use this dictionary to find the best move. Only once the best move was found would the game board be updated. This solved the problem. This version of the game became Hard mode (impossible).  

Now that I have an Easy and Hard mode it made sense to have a 'medium mode' as well. This version of the game used a combination of the hard and easy modes. The computers first turn would use minimax, its second turn would use the pick random function and then the third turn would use minimax again. This pattern was repeated for any further turns.  

Once all these were created, I was left with 5 separate .py files which I need to combine into one. As I had used the previous code of each game as a template, I found myself with a lot of duplicated functions and variables. I then preceded to slimline the code removing any repeated functions and variables. This posed its own set of problems as some parts of the code no longer recognised each other. But I got there eventually. There are still a few duplications, but I feel they were necessary. 

 