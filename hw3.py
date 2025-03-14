"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""

from typing import List


def tic_tac_toe(board: List[List[str]]) -> str:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return f"{board[i][0]} wins!"
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return f"{board[0][i]} wins!"

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return f"{board[0][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return f"{board[0][2]} wins!"

    for row in board:
        if "-" in row:
            return "unfinished!"

    return "draw!"


board1 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]
print("1:", tic_tac_toe(board1))

board2 = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
print("2:", tic_tac_toe(board2))
