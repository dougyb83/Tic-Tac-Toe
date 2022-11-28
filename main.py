from tkinter import *
from tkinter import messagebox
import random

# Set the player pieces and chose a random piece for the user to play with
player_pieces = ["X", "O"]
player = random.choice(player_pieces)

# Keep track of the current players piece (X or O)
current_player = ""
# Used in the computers_turn function
random_count = 0

# For games against the computer, this sets the computers piece to be the opposite of the players piece
if player == "X":
    computer = "O"
else:
    computer = "X"

# Keeps track of piece positions on the board for minimax to check against
board_dict = {
    "a1": " ", "a2": " ", "a3": " ",
    "a4": " ", "a5": " ", "a6": " ",
    "a7": " ", "a8": " ", "a9": " "}

# Keeps track of board clicks to help confirm which player is currently playing
clicked = True
# Counts how many turns the player have had
count = 0


# Loads the splash screen/main menu in Tkinter
def splash_screen():
    # Splash screen
    splash_root = Tk()
    splash_root.title("Splash Screen!!")

    # Background image
    splash_img = PhotoImage(file="background.png")
    canvas = Canvas(splash_root, width=600, height=411)
    canvas.pack(fill="both", expand=True)

    # Display background image
    canvas.create_image(0, 0, image=splash_img, anchor="nw")

    # Set height and width of window
    app_height = 411
    app_width = 600

    # Get screen dimensions
    screen_height = splash_root.winfo_screenheight()
    screen_width = splash_root.winfo_screenwidth()

    # Calculate centered screen position
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    # Place window in center of screen
    splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # Hide the title bar
    splash_root.overrideredirect(True)

    # Create buttons to select game difficulty or exit game
    pl2pl = Button(splash_root, text="Play", font=("Arial", 10, "bold"), bg="grey", fg="black", borderwidth=10,
                   height=1, width=15,
                   command=lambda: [splash_root.destroy(), p2p()])
    p2cEasy = Button(splash_root, text="Let's Go", font=("Arial", 10, "bold"), bg="grey", fg="black", borderwidth=10,
                     height=1, width=15,
                     command=lambda: [splash_root.destroy(), p2cE()])
    p2cMedium = Button(splash_root, text="Ok Then", font=("Arial", 10, "bold"), bg="grey", fg="black", borderwidth=10,
                       height=1, width=15,
                       command=lambda: [splash_root.destroy(), p2cM()])
    p2cHard = Button(splash_root, text="Let's Go", font=("Arial", 10, "bold"), bg="grey", fg="black", borderwidth=10,
                     height=1, width=15,
                     command=lambda: [splash_root.destroy(), p2cH()])
    exit_game = Button(splash_root, text="Exit Game", font=("Arial", 10, "bold"), bg="grey", fg="black", borderwidth=10,
                       height=1, width=15,
                       command=lambda: splash_root.destroy())

    # set button positions
    pl2pl.place(x=30, y=50)
    p2cEasy.place(x=30, y=150)
    p2cMedium.place(x=30, y=250)
    p2cHard.place(x=30, y=350)
    exit_game.place(x=420, y=340)

    # text above p2p button
    canvas.create_text(100, 30, text="Play Against A Friend", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(103, 33, text="Play Against A Friend", fill="white", font=("Arial", 12, "bold"))

    # text above p2cE button
    canvas.create_text(100, 130, text="EASY vs Computer", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(103, 133, text="EASY vs Computer", fill="white", font=("Arial", 12, "bold"))

    # text above p2cM button
    canvas.create_text(100, 230, text="MEDIUM vs Computer", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(103, 233, text="MEDIUM vs Computer", fill="white", font=("Arial", 12, "bold"))

    # text above p2cH button
    canvas.create_text(100, 330, text="HARD vs Computer", fill="black", font=("Arial", 12, "bold"))
    canvas.create_text(103, 333, text="HARD vs Computer", fill="white", font=("Arial", 12, "bold"))

    # Game description, how to play
    canvas.create_text(300, 140, text="How to Play", fill="black", font=("Arial", 20, "bold"))
    canvas.create_text(302, 142, text="How to Play", fill="white", font=("Arial", 20, "bold"))
    canvas.create_text(380, 210, text="Click on a tile to place your marker!\nTo win place three markers in a row!\n"
                                      "A winning row can be horizontal,\nvertical or diagonal", fill="black",
                       font=("Arial", 15))
    canvas.create_text(382, 212, text="Click on a tile to place your marker!\nTo win place three markers in a row!\n"
                                      "A winning row can be horizontal,\nvertical or diagonal", fill="white",
                       font=("Arial", 15))
    # Game title
    canvas.create_text(370, 40, text="TIC TAC TOE", fill="black", font=("Arial", 30, "bold", "italic"))
    canvas.create_text(376, 46, text="TIC TAC TOE", fill="black", font=("Arial", 30, "bold", "italic"))
    canvas.create_text(373, 43, text="TIC TAC TOE", fill="white", font=("Arial", 30, "bold", "italic"))

    splash_root.mainloop()


# loads the person vs person game in Tkinter
def p2p():
    global turn
    root = Tk()
    root.title("TIC TAC TOE")
    root.iconbitmap("tictactoe.ico")

    # Loads the game window
    def reset():
        global reset_game, b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count, player, computer
        clicked = True
        # picks a random piece for the player
        player = random.choice(player_pieces)
        # resets turn count to 0
        count = 0
        # tells the player their game piece. X or O
        turn.config(text=("You're " + player + ",s"), fg="black", font=("Arial", 25, "bold"))
        # Main menu button returns to the splash screen
        main_menu = Button(root, text="Main Menu", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                           height=1, width=10,
                           command=lambda: [root.destroy(), splash_screen()])
        # clears the game board
        reset_game = Button(root, text="Reset Game", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                            height=1, width=10, command=lambda: reset())

        # creates clickable buttons to place players piece on the board
        b1 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b9))

        # sets the positions of the main menu, reset and game buttons
        main_menu.grid(row=0, column=0, columnspan=2, pady=20)
        reset_game.grid(row=0, column=1, columnspan=2, pady=20)
        turn.grid(row=1, column=0, columnspan=3)
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)

        b4.grid(row=4, column=0)
        b5.grid(row=4, column=1)
        b6.grid(row=4, column=2)

        b7.grid(row=5, column=0)
        b8.grid(row=5, column=1)
        b9.grid(row=5, column=2)

    # When a button is clicked this function is called
    def b_click(b):
        global clicked, count, player, current_player
        current_player = player
        # checks if the board square is empty and if its player ones turn. if it is then the players piece is placed
        if b["text"] == " " and clicked is True:
            b["text"] = player
            # check if there is a winner
            final_check_winner(player)
            # Increases turn count by 1
            count += 1
            # Check the board for a draw
            check_draw(player)
            # changes the player piece ready for player twos turn
            if player == "X":
                player = "O"
            else:
                player = "X"
            # sets clicked to false to indicate who's turn it is
            clicked = False
            # Displays who's turn it is
            turn.config(text=(player + "'s turn"), fg="black", font=("Arial", 25, "bold"))
        # checks if the board square is empty and if its player two's turn. if it is then the players piece is placed
        elif b["text"] == " " and clicked is False:
            b["text"] = player
            # check if there is a winner
            final_check_winner(player)
            # Increases turn count by 1
            count += 1
            # Check the oard for a draw
            check_draw(player)
            # changes the player piece ready for player twos turn
            if player == "X":
                player = "O"
            else:
                player = "X"
            # sets clicked to true to indicate who's turn it is
            clicked = True
            # Displays who's turn it is
            turn.config(text=(player + "'s turn"), fg="black", font=("Arial", 25, "bold"))
        # If neither condition is met display an error message
        else:
            messagebox.showerror("TIC TAC TOE", "Cant go there!!!!!\nPick another space!")

    # creates the label to display players turn
    turn = Label(text=player + "'s turn", font=('consolas,40'))
    turn.grid(row=1, column=0, columnspan=3)

    reset()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


# loads the person vs computer game in Tkinter. Easy mode - computer picks random place on the board
def p2cE():
    global turn
    root = Tk()
    root.title("TIC TAC TOE")
    root.iconbitmap("tictactoe.ico")

    # When called, resets the game board and variables
    def reset():
        global reset_game, b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count, player, computer, turn
        clicked = True
        # picks a random piece for the player
        player = random.choice(player_pieces)
        # resets turn count to 0
        count = 0
        # this sets the computers piece to be the opposite of the players piece
        if player == "X":
            computer = "O"
        else:
            computer = "X"
        # resets turn count to 0
        count = 0
        # tells the player their game piece. X or O
        turn.config(text=("You're " + player + ",s"), fg="black", font=("Arial", 25, "bold"))
        # Main menu button returns to the splash screen
        main_menu = Button(root, text="Main Menu", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                           height=1, width=10,
                           command=lambda: [root.destroy(), splash_screen()])
        # clears the game board
        reset_game = Button(root, text="Reset Game", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                            height=1, width=10, command=lambda: reset())
        # creates clickable buttons to place players piece on the board
        b1 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, borderwidth=10,
                    bg="SystemButtonFace", command=lambda: b_click(b9))
        # sets the positions of the main menu, reset and game buttons
        main_menu.grid(row=0, column=0, columnspan=2, pady=20)
        reset_game.grid(row=0, column=1, columnspan=2, pady=20)
        turn.grid(row=1, column=0, columnspan=3)
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)

        b4.grid(row=4, column=0)
        b5.grid(row=4, column=1)
        b6.grid(row=4, column=2)

        b7.grid(row=5, column=0)
        b8.grid(row=5, column=1)
        b9.grid(row=5, column=2)

    # When a button is clicked this function is called
    def b_click(b):
        global clicked, count, player, computer, current_player, b1, b2, b3, b4, b5, b6, b7, b8, b9
        current_player = player
        # checks if the clicked board square is empty and if it is player ones turn (clicked = True).
        # if it is then the players piece is placed
        if b["text"] == " " and clicked is True:
            b["text"] = player
            # check if there is a winner
            final_check_winner(player)
            # Increases turn count by 1
            count += 1
            # Check the board for a draw
            check_draw(player)
            # sets clicked to false to indicate who's turn it is
            clicked = False
            # Displays who's turn it is
            turn.config(text=("Computers turn"), fg="black", font=("Arial", 25, "bold"))
            # Waits for a second to give illusion of computer thinking about next move
            # Then calls the computer_pick_random function
            root.after(1100, computer_pick_random)
        # If condition is not met display an error message
        else:
            messagebox.showerror("TIC TAC TOE", "Cant go there!!!!!\nPick another space!")

    def computer_pick_random():
        global clicked, count, player, computer, current_player, b1, b2, b3, b4, b5, b6, b7, b8, b9
        # Sets the current player to be displayed on turn.config
        current_player = "Computer"
        # A list of all the possible board positions
        button_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        # Picks a random board position
        b = random.choice(button_list)

        # Checks if the random board position is free. If it is, the piece is placed on that position
        # if not then a new random board position is chosen until a free space is found
        while True:
            if b["text"] == " " and clicked is False:
                b["text"] = computer
                # check if there is a winner
                final_check_winner(computer)
                # Increases turn count by 1
                count += 1
                # Check the board for a draw
                check_draw(computer)
                # sets clicked to true to indicate who's turn it is
                clicked = True
                # Displays who's turn it is
                turn.config(text=(player + "'s turn"), fg="black", font=("Arial", 25, "bold"))
                break
            else:
                # if position taken, choose another randon position
                b = random.choice(button_list)

    # creates the label to display players turn
    turn = Label(text=player + "'s turn", font=('consolas,40'))
    turn.grid(row=1, column=0, columnspan=3)

    reset()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


# loads the person vs computer game in Tkinter. Medium mode - uses a combination of picking a random position or
# minimax picking a position
def p2cM():
    global turn
    root = Tk()
    root.title("TIC TAC TOE")
    root.iconbitmap("tictactoe.ico")

    # When called, resets the game board and variables
    def reset():
        global reset_game, b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count, player, computer, board_dict, turn
        clicked = True
        # picks a random piece for the player
        player = random.choice(player_pieces)
        # this sets the computers piece to be the opposite of the players piece
        if player == "X":
            computer = "O"
        else:
            computer = "X"
        # resets turn count to 0
        count = 0
        # dictionary to keep track of pieces onn the game board for minimax to check against
        board_dict = {
            "a1": " ", "a2": " ", "a3": " ",
            "a4": " ", "a5": " ", "a6": " ",
            "a7": " ", "a8": " ", "a9": " "}
        # tells the player their game piece. X or O
        turn.config(text=("You're " + player + ",s"), fg="black", font=("Arial", 25, "bold"))
        # Main menu button returns to the splash screen
        main_menu = Button(root, text="Main Menu", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                           height=1, width=10,
                           command=lambda: [root.destroy(), splash_screen()])
        # clears the game board
        reset_game = Button(root, text="Reset Game", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                            height=1, width=10, command=lambda: reset())
        # creates clickable buttons to place players piece on the board
        b1 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b1, "a1"))
        b2 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b2, "a2"))
        b3 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b3, "a3"))

        b4 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b4, "a4"))
        b5 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b5, "a5"))
        b6 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b6, "a6"))

        b7 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b7, "a7"))
        b8 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b8, "a8"))
        b9 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b9, "a9"))
        # sets the positions of the main menu, reset and game buttons
        main_menu.grid(row=0, column=0, columnspan=2, pady=20)
        reset_game.grid(row=0, column=1, columnspan=2, pady=20)
        turn.grid(row=1, column=0, columnspan=3)
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)

        b4.grid(row=4, column=0)
        b5.grid(row=4, column=1)
        b6.grid(row=4, column=2)

        b7.grid(row=5, column=0)
        b8.grid(row=5, column=1)
        b9.grid(row=5, column=2)

    # When a button on the game board is clicked this function is called
    def b_click(b, a):
        global clicked, count, player, computer, current_player
        current_player = player
        # checks if the clicked board square is empty and if it is player ones turn (clicked = True).
        # if it is then the players piece is placed
        if b["text"] == " " and clicked is True:
            b["text"] = player
            # updates the board dictionary with the current played piece
            board_dict[a] = player
            # check if there is a winner
            final_check_winner(player)
            # Check the board for a draw
            count += 1
            # Check the board for a draw
            check_draw(player)
            # sets clicked to false to indicate who's turn it is
            clicked = False
            # Displays who's turn it is
            turn.config(text=("Computers turn"), fg="black", font=("Arial", 25, "bold"))
            # Waits for a second to give illusion of computer thinking about next move
            # Then calls the computers_turn function
            root.after(1000, computers_turn)
        # If condition is not met display an error message
        else:
            messagebox.showerror("TIC TAC TOE", "Cant go there!!!!!\nPick another space!")

    # Function that determines if AI_turn or computer_pick_random is used for the computers turn
    def computers_turn():
        global random_count
        if random_count == 0:
            random_count += 1
            AI_turn()
        elif random_count == 1:
            random_count += 1
            computer_pick_random()
        else:
            random_count = 0
            AI_turn()

    # picks a random position on the board for the computers turn
    def computer_pick_random():
        global clicked, count, player, computer, current_player, b1, b2, b3, b4, b5, b6, b7, b8, b9
        # Sets the current player to be displayed on turn.config
        current_player = "Computer"
        # A list of all the possible board positions
        button_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        # Picks a random board position
        b = random.choice(button_list)
        # Dictionary that links the button reference to the board_dict positions.
        button_dict = {
            "a1": b1, "a2": b2, "a3": b3,
            "a4": b4, "a5": b5, "a6": b6,
            "a7": b7, "a8": b8, "a9": b9}

        # Checks if the random board position is free. If it is, the piece is placed on that position
        # if not then a new random board position is chosen until a free space is found
        while True:
            if b["text"] == " " and clicked is False:
                b["text"] = computer
                # Finds the randomly selected board position (ie b1) in button_dict. if the button ref matches a value
                # the key (ie a1) is then used to update the board_dict
                for key, value in button_dict.items():
                    if b == value:
                        board_dict[key] = computer
                # check if there is a winner
                final_check_winner(computer)
                # Increases turn count by 1
                count += 1
                # Check the board for a draw
                check_draw(computer)
                # sets clicked to true to indicate who's turn it is
                clicked = True
                # Displays who's turn it is
                turn.config(text=(player + "'s turn"), fg="black", font=("Arial", 25, "bold"))
                break
            else:
                # if position taken, choose another randon position
                b = random.choice(button_list)

    # creates the label to display players turn
    turn = Label(text=player + "'s turn", font=('consolas,40'))
    turn.grid(row=1, column=0, columnspan=3)

    reset()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


# loads the person vs computer game in Tkinter. Hard mode - uses minimax
def p2cH():
    global turn
    root = Tk()
    root.title("TIC TAC TOE")
    root.iconbitmap("tictactoe.ico")

    def reset():
        global reset_game, b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count, player, computer, board_dict, turn
        clicked = True
        # picks a random piece for the player
        player = random.choice(player_pieces)
        # this sets the computers piece to be the opposite of the players piece
        if player == "X":
            computer = "O"
        else:
            computer = "X"
        # resets turn count to 0
        count = 0
        # dictionary to keep track of pieces onn the game board for minimax to check against
        board_dict = {
            "a1": " ", "a2": " ", "a3": " ",
            "a4": " ", "a5": " ", "a6": " ",
            "a7": " ", "a8": " ", "a9": " "}
        # tells the player their game piece. X or O
        turn.config(text=("You're " + player + ",s"), fg="black", font=("Arial", 25, "bold"))
        # Main menu button returns to the splash screen
        main_menu = Button(root, text="Main Menu", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                           height=1, width=10,
                           command=lambda: [root.destroy(), splash_screen()])
        # clears the game board
        reset_game = Button(root, text="Reset Game", font=("Arial", 11, "bold"), bg="grey", fg="black", borderwidth=10,
                            height=1, width=10, command=lambda: reset())
        # creates clickable buttons to place players piece on the board
        b1 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b1, "a1"))
        b2 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b2, "a2"))
        b3 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b3, "a3"))

        b4 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b4, "a4"))
        b5 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b5, "a5"))
        b6 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b6, "a6"))

        b7 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b7, "a7"))
        b8 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b8, "a8"))
        b9 = Button(root, text=" ", font=("Helvetica", 50), height=1, width=3, bg="SystemButtonFace", borderwidth=10,
                    command=lambda: b_click(b9, "a9"))
        # sets the positions of the main menu, reset and game buttons
        main_menu.grid(row=0, column=0, columnspan=2, pady=20)
        reset_game.grid(row=0, column=1, columnspan=2, pady=20)
        turn.grid(row=1, column=0, columnspan=3)
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)

        b4.grid(row=4, column=0)
        b5.grid(row=4, column=1)
        b6.grid(row=4, column=2)

        b7.grid(row=5, column=0)
        b8.grid(row=5, column=1)
        b9.grid(row=5, column=2)

    # When a button on the game board is clicked this function is called
    def b_click(b, a):
        global clicked, count, player, computer, current_player
        current_player = player
        # checks if the clicked board square is empty and if it is player ones turn (clicked = True).
        # if it is then the players piece is placed
        if b["text"] == " " and clicked is True:
            b["text"] = player
            # updates board_dict with the players chosen position
            board_dict[a] = player
            final_check_winner(player)
            # Increases turn count by 1
            count += 1
            # Check the board for a draw
            check_draw(player)
            # sets clicked to false to indicate who's turn it is
            clicked = False
            # Displays who's turn it is
            turn.config(text=("Computers turn"), fg="black", font=("Arial", 25, "bold"))
            # Waits for a second to give illusion of computer thinking about next move
            # Then calls the computer_pick_random function
            root.after(1000, AI_turn)
        else:
            # If neither condition is met display an error message
            messagebox.showerror("TIC TAC TOE", "Cant go there!!!!!\nPick another space!")

    # creates the label to display players turn
    turn = Label(text=player + "'s turn", font=('consolas,40'))
    turn.grid(row=1, column=0, columnspan=3)

    reset()
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def AI_turn():
    global clicked, count, player, computer, current_player
    current_player = "Computer"
    bestscore = -1000
    bestmove = " "
    # Dictionary that links the button reference to the board_dict positions.
    button_dict = {
        "a1": b1, "a2": b2, "a3": b3,
        "a4": b4, "a5": b5, "a6": b6,
        "a7": b7, "a8": b8, "a9": b9}
    # runs the minimax algorithm checking every possible winning move to decide the next best move
    for key in board_dict.keys():
        if board_dict[key] == " " and clicked is False:
            board_dict[key] = computer
            score = minimax(board_dict, 0, False)
            board_dict[key] = " "
            if score > bestscore:
                bestscore = score
                bestmove = key

    # updates board_dict with the best move selected by minimax
    board_dict[bestmove] = computer
    # assign the button ref to ai_choice
    ai_choice = button_dict[bestmove]
    # set the button text to the computers piece
    ai_choice["text"] = computer
    # check if there is a winner
    final_check_winner(computer)
    # Increases turn count by 1
    count += 1
    # Check the board for a draw
    check_draw(computer)
    # sets clicked to true to indicate who's turn it is
    clicked = True
    # Displays who's turn it is
    turn.config(text=(player + "'s turn"), fg="black", font=("Arial", 25, "bold"))


# minimax algorithm
def minimax(board, depth, isMaximizing):
    global computer, player
    if check_winner(computer):
        return 1
    elif check_winner(player):
        return -1
    elif minimax_check_draw():
        return 0

    if (isMaximizing):
        bestscore = -1000
        for key in board_dict.keys():
            if board_dict[key] == " ":
                board_dict[key] = computer
                score = minimax(board, depth + 1, False)
                board_dict[key] = " "
                if score > bestscore:
                    bestscore = score
        return bestscore
    else:
        bestscore = 1000
        for key in board_dict.keys():
            if board_dict[key] == " ":
                board_dict[key] = player
                score = minimax(board, depth + 1, True)
                board_dict[key] = " "
                if score < bestscore:
                    bestscore = score
        return bestscore


# function just for minimax to check if there is a draw
def minimax_check_draw():
    for key in board_dict.keys():
        if board_dict[key] == " ":
            return False
    return True


# function just for minimax to check if there is a winner
def check_winner(piece):
    # ACROSS
    if board_dict["a7"] == board_dict["a8"] == board_dict["a9"] == piece:
        return True
    elif board_dict["a4"] == board_dict["a5"] == board_dict["a6"] == piece:
        return True
    elif board_dict["a1"] == board_dict["a2"] == board_dict["a3"] == piece:
        return True
    # DOWN
    elif board_dict["a7"] == board_dict["a4"] == board_dict["a1"] == piece:
        return True
    elif board_dict["a8"] == board_dict["a5"] == board_dict["a2"] == piece:
        return True
    elif board_dict["a9"] == board_dict["a6"] == board_dict["a3"] == piece:
        return True
    # DIAGONAL
    elif board_dict["a7"] == board_dict["a5"] == board_dict["a3"] == piece:
        return True
    elif board_dict["a9"] == board_dict["a5"] == board_dict["a1"] == piece:
        return True
    else:
        return False


# checks if there is a draw. if there is it highlights all buttons in orange and calls the disable_buttons function
def check_draw(player):
    global count
    if count == 9 and check_winner(player) is False:
        for x in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
            x.config(bg="orange")
        turn.config(text=("DRAW!!!"), fg="red", font=("Arial", 25, "bold"))
        disable_buttons()
        reset_game.wait_variable()


# check if there is a winner. if there is the highlight winner function is called
def final_check_winner(piece):
    # ACROSS
    if b1["text"] == b2["text"] == b3["text"] == piece:
        highlight_winner(b1, b2, b3)
        return True
    elif b4["text"] == b5["text"] == b6["text"] == piece:
        highlight_winner(b4, b5, b6)
        return True
    elif b7["text"] == b8["text"] == b9["text"] == piece:
        highlight_winner(b7, b8, b9)
        return True
    # DOWN
    elif b1["text"] == b4["text"] == b7["text"] == piece:
        highlight_winner(b1, b4, b7)
        return True
    elif b2["text"] == b5["text"] == b8["text"] == piece:
        highlight_winner(b2, b5, b8)
        return True
    elif b3["text"] == b6["text"] == b9["text"] == piece:
        highlight_winner(b3, b6, b9)
        return True
    # DIAGONAL
    elif b1["text"] == b5["text"] == b9["text"] == piece:
        highlight_winner(b1, b5, b9)
        return True
    elif b3["text"] == b5["text"] == b7["text"] == piece:
        highlight_winner(b3, b5, b7)
        return True
    else:
        return False


# highlights the winning row in green and calls the disable_buttons function
def highlight_winner(x, y, z):
    global player, reset_game, current_player
    x.config(bg="green")
    y.config(bg="green")
    z.config(bg="green")
    turn.config(text=(current_player + " WINS!!"), fg="green", font=("Arial", 25, "bold"))
    disable_buttons()
    reset_game.wait_variable()


# disables the board buttons
def disable_buttons():
    for x in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        x.config(state=DISABLED)


splash_screen()
