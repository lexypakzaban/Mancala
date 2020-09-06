def reset():
    global board_spaces, whose_turn_is_it,  game_is_still_playing
    board_spaces = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    whose_turn_is_it = 1
    game_is_still_playing = True


def draw_board():
    """
    draws the board
    :return:
    """
    #Note: in a few of the lines ahead, we are using the notation {0:2d} instead of just {0}. The additional stuff is
    #      formatting info - it says that we want an integer (the "d" - don't ask me why) that is at least two characters
    #      wide. If it is a single digit number, put a space in front of it. This will ensure that our boxes will look
    #      right, whether they hold single or double digit numbers!
    print("") # blank line
    print(" P2  13  12  11  10   9   8  ")
    print("+---+---+---+---+---+---+---+---+")
    print("|   |{0:2d} |{1:2d} |{2:2d} |{3:2d} |{4:2d} |{5:2d} |   |".format(board_spaces[13],board_spaces[12],\
                                                                             board_spaces[11],board_spaces[10],\
                                                                             board_spaces[9],board_spaces[8]))
    print("|{0:2d} +---+---+---+---+---+---+{1:2d} |".format(board_spaces[0],board_spaces[7]))
    print("|   |{0:2d} |{1:2d} |{2:2d} |{3:2d} |{4:2d} |{5:2d} |   |".format(board_spaces[1],board_spaces[2],\
                                                                             board_spaces[3],board_spaces[4],\
                                                                             board_spaces[5],board_spaces[6]))
    print("+---+---+---+---+---+---+---+---+")
    print("      1   2   3   4   5   6  P1")

def p1_ply():
    """
    handles one move for player 1
    :return: whether the player gets to go again.
    """
    good_answer = False
    while not good_answer:
        try:
            which_bin = int(input("Player 1, which bin do you want, 1-6? "))
            if which_bin > 0 and which_bin < 7:
                good_answer = True
            else:
                print("That is not a legal move.")
        except ValueError:
            print("That was not a number. Please try again.")

    # by the time we get here, the variable "which_bin" holds a legal move - which bin the player wants.


    # TODO: #1:
    #       The player has chosen a legal move - a number stored in the variable "which_bin." Put the number of
    #       chips in this space on the board into a new variable, "num_chips_to_distribute," and then empty this space on
    #       the board.

    num_chips_to_distribute = board_spaces[which_bin]
    board_spaces[which_bin] = 0

    drop_location = which_bin  # this is the variable that we will use to drop 1 chip each in several spaces.

    while num_chips_to_distribute > 0:
        # TODO: #2:
        # Increment the drop_location; if we get to 14, reset it to zero.
        # (Hint: you can do the "14 check" with an "if" statement or use a "%" trick.)

        drop_location = drop_location + 1
        if drop_location > 13:
            drop_location = 0

        # TODO: #3:
        #   If drop_location is not on the opponent's scoring space, add one chip to this board space, and
        #   reduce num_chips_to_distribute by 1.
        if drop_location != 0:
            board_spaces[drop_location] = board_spaces [drop_location] + 1

            num_chips_to_distribute = num_chips_to_distribute - 1


    # ----- after the while loop....
# TODO: #4:  Implements rules #07 & #08. Skip this and come back to it, if you are intimidated.
    # TODO: #4.1:
    # Check whether the drop_location wound up on Player 1's side of the board.
    if drop_location < 7 and drop_location > 0:
    #   TODO: #4.2:
    #   If so:
            # check whether there is now exactly one chip in the drop_location - that means it was previously empty.
        if board_spaces[drop_location] == 1:
            #   TODO: #4.3:
            #   a) add this chip to the P1 scoring goal,
            board_spaces[7] = board_spaces[7] + 1
            #   b) remove the chip from the drop_location,
            board_spaces[drop_location] = board_spaces[drop_location] - 1
            #   c) Figure out what the opposite bin is from the one where drop_location wound up and put this number into
            #       a new variable, "opposite_bin."
            #       Note: there is a mathematical pattern between each bin and it's opposite. Can you figure it out?
            opposite_bin = 14 - drop_location
            #   d) find out how many chips are in the opposite_bin space and put them in scoring zone
            if board_spaces[opposite_bin] > 0:
                board_spaces[7] = board_spaces[7] + board_spaces[opposite_bin]
            #   e) remove the chips from the opposite_bin space
                board_spaces[opposite_bin] = 0

        # TODO: #4.4:
        # if we landed in our own scoring bin, then return True to indicate that player 1 moves again.
    if drop_location == 7:
        return True
    return False  # otherwise - if we wound up other than on player 1's side of board. - Now it will be Player 2's turn.

def p2_ply():
    good_answer = False
    while not good_answer:
        try:
            which_bin = int(input("Player 2, which which_bin do you want, 8-13? "))
            if which_bin > 7 and which_bin < 14:
                good_answer = True
            else:
                print("That is not a legal move.")
        except ValueError:
            print("That was not a number. Please try again.")

    #by the time we get here, the variable "which_bin" holds a legal move - which bin the player wants.

        # TODO: #5:
        #       The player has chosen a legal move - a number stored in the variable "which_bin." Put the number of
        #       chips in this space on the board into a new variable, "num_chips_to_distribute," and then empty this space on
        #       the board.

    num_chips_to_distribute = board_spaces[which_bin]
    board_spaces[which_bin] = 0



    drop_location = which_bin  # this is the variable that we will use to drop 1 chip each in several spaces.

    while num_chips_to_distribute > 0:
        # TODO: #6:
        # Increment the drop_location; if we get to 14, reset it to zero.
        # (Hint: you can do the "14 check" with an "if" statement or use a "%" trick.)

        drop_location = drop_location + 1
        if drop_location > 13:
            drop_location = 0

        # TODO: #7:
        #   If drop_location is not on the opponent's scoring space, add one chip to this board space, and
        #   reduce num_chips_to_distribute by 1.

        if drop_location != 7:
            board_spaces[drop_location] = board_spaces[drop_location] + 1

            num_chips_to_distribute = num_chips_to_distribute - 1

    # ----- after the while loop....
    # TODO: #8: Implements rules #07 & #08. Skip this and come back to it, if you are intimidated.
    # TODO: #8.1:
    # Check whether the drop_location wound up on Player 2's side of the board.
    if drop_location < 14 and drop_location > 7:
    #   TODO: #8.2:
    #   If so: check whether there is now exactly one chip in the drop_location - that means it was previously empty.
        if board_spaces[drop_location] == 1:
    #       TODO: #8.3:
    #       If it was previously empty and it isn't player 2's scoring goal, then
            drop_location != 7
            #   TODO: #8.4:
            #   a) add this chip to the P2 scoring goal,
            board_spaces[0] = board_spaces[0] + 1
            #   b) remove the chip from the drop_location,
            board_spaces[drop_location] = board_spaces[drop_location] - 1
            #   c) Figure out what the opposite bin is from the one where drop_location wound up and put this number into
            #       a new variable, "opposite_bin."
            #       Note: there is a mathematical pattern between each bin and it's opposite. Can you figure it out?
            opposite_bin = 14 - drop_location
            #   d) find out how many chips are in the opposite_bin space and put them in scoring zone
            if board_spaces[opposite_bin] > 0:
                board_spaces[0] = board_spaces[0] + board_spaces[opposite_bin]
            #   e) remove the chips from the opposite_bin space
                board_spaces[opposite_bin] = 0

        # TODO: #8.5:
        # return True - since we have landed on Player 2's side. - Player 2 gets to move again.
        # Note: this happens if the drop_location wound up on Player 2's side, regardless of whether there was one
        #       chip. Set the indentation of this line accordingly!
            return True

    return False  # otherwise - if we wound up other than on player 2's side of board. - Now it will be Player 1's turn.

def check_for_game_over():
    """
    checks to see whether all the squares are empty on either side of the board.
    :return: whether the game should end.
    """
    sum_of_p1_spaces = 0
    sum_of_p2_spaces = 0

    # TODO: #9: Find the sum of all the chips stored in spaces 1-6 and put it into "sum_of_p1_spaces."
    # you can do this by brute force or use a loop.
    for x in range(1,7):
        sum_of_p1_spaces = sum_of_p1_spaces + board_spaces[x]
    #print(sum_of_p1_spaces)

    # TODO: #10: Find the sum of all the chips stored in spaces 8-13 and put it into "sum_of_p2_spaces."
    # you can do this by brute force or use a loop.
    for x in range(8,14):
        sum_of_p2_spaces = sum_of_p2_spaces + board_spaces[x]
    #print(sum_of_p2_spaces)


    if sum_of_p1_spaces == 0:
        return True
    if sum_of_p2_spaces == 0:
        return True

    return False # if we got this far, then the game isn't over.

def give_players_pieces_on_their_side_of_the_board():
    """
    gives player 1 all the pieces in squares 1-6 and gives player 2 all the pieces in squares 8-13.
    :return: None
    """

    #Note: this is very similar to check_for_game_over() - you can probably steal some code from that and modify.
    sum_of_p1_spaces = 0
    sum_of_p2_spaces = 0

    # TODO: #11: Find the sum of all the chips stored in spaces 1-6 and put it into sum_of_p1_spaces. Then put that number of chips into player 1's goal bin.
    # you can do this by brute force or use a loop.
    for x in range(1,7):
        sum_of_p1_spaces = sum_of_p1_spaces + board_spaces[x]
    print(sum_of_p1_spaces)


    board_spaces[7] = board_spaces[7] + sum_of_p1_spaces

    # TODO: #12: Find the sum of all the chips stored in spaces 8-13 and put it into sum_of_p2_spaces. Then put that number of chips into player 2's goal bin.
    # you can do this by brute force or use a loop.
    for x in range(8,14):
        sum_of_p2_spaces = sum_of_p2_spaces + board_spaces[x]
    print(sum_of_p2_spaces)

    board_spaces[0] = board_spaces[0] + sum_of_p2_spaces

    # TODO: #13: Empty all the bins 1-6 and 8-13.

    board_spaces[1] = 0
    board_spaces[2] = 0
    board_spaces[3] = 0
    board_spaces[4] = 0
    board_spaces[5] = 0
    board_spaces[6] = 0

    board_spaces[8] = 0
    board_spaces[9] = 0
    board_spaces[10] = 0
    board_spaces[11] = 0
    board_spaces[12] = 0
    board_spaces[13] = 0

def loop():
    """
    perform a single ply and check whether the game is over.
    :return: None
    """
    global whose_turn_is_it, game_is_still_playing
    draw_board()
    if whose_turn_is_it == 1:
        go_again = p1_ply()
        if not go_again:
            whose_turn_is_it = 2
    else:
        go_again = p2_ply()
        if not go_again:
            whose_turn_is_it = 1
    game_is_still_playing = not check_for_game_over()


def main():
    """
    Reset the board, run the primary game loop, and handle the post-game summary.
    :return: None
    """
    reset()
    while game_is_still_playing:
        loop()
    draw_board()
    print ("Reallocating pieces.")
    give_players_pieces_on_their_side_of_the_board()
    draw_board()
    print ("Game over.")

    # TODO: #14: Look at the number of chips stored in spaces 7 and 0 in our board_spaces list - use this to indicate who won or if it is a draw.
    if board_spaces[7] > board_spaces[0]:
        print("Player 1 won!")
    if board_spaces[0] > board_spaces[7]:
        print("Player 2 won!")
    if board_spaces[7] == board_spaces[0]:
        print ("It's a tie!")

# =============================  Game Starts here. =====================================
main()
