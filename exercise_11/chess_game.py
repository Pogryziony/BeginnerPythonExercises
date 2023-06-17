# "K" - król, "Q" - królowa, "R" - wieża, "B" - goniec, "N" - skoczek, "P" - pionek, "-" - puste pole.
import pprint


def chess_game():
    board = [['R' if (row, column) in [(0, 0), (0, 7)]
              else 'N' if (row, column) in [(0, 1), (0, 6)]
              else 'B' if (row, column) in [(0, 2), (0, 5)]
              else 'Q' if (row, column) == (0, 3)
              else 'K' if (row, column) == (0, 4)
              else 'P' if row == 1
              else 'r' if (row, column) in [(7, 0), (7, 7)]
              else 'n' if (row, column) in [(7, 1), (7, 6)]
              else 'b' if (row, column) in [(7, 2), (7, 5)]
              else 'q' if (row, column) == (7, 3)
              else 'k' if (row, column) == (7, 4)
              else 'p' if row == 6
              else '-' for column in range(8)] for row in range(8)
             ]

    pprint.pprint(board)


chess_game()
