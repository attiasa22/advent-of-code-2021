"""Day 4 of https://adventofcode.com 2021 challenge"""
import numpy as np

def find_winning_bingo(games_and_drawings):
    '''Find the winning bingo game given an order of drawings'''

    boards, drawings = create_boards(games_and_drawings)

    winning_boards, drawn_numbers = get_winning_board( boards, drawings)
    
    # Part 1
    board_sum_1 = np.sum(winning_boards[0].astype(np.int))
    
    # Part 2
    board_sum_2 = np.sum(winning_boards[-1].astype(np.int))
    
    return board_sum_1 * drawn_numbers[0], board_sum_2 * drawn_numbers[-1]

def get_winning_board(boards, drawings):
    winning_boards = []
    winning_drawings = []
    
    while len(drawings):
        drawn_number = drawings.pop(0)
        for board in boards:
            location = np.where(board == str(drawn_number))
            if len(location[0]):
                if check_columns(board) is None and check_rows(board) is None:
                    board[location[0][0]][location[1][0]] = 0

                if (check_columns(board) is not None or check_rows(board) is not None) and not next((True for elem in winning_boards if elem is board), False) :
                    winning_boards.append(board)
                    winning_drawings.append(drawn_number)
                
    print(np.shape(winning_boards))   
    return winning_boards, winning_drawings               

def check_columns(board):
    for column in board:
        if len(set(column)) == 1 and column[0] is not None:
            return column[0]
    return None

def check_rows(board):
    return check_columns(zip(*reversed(board)))  # rotate the board 90 degrees

def create_boards(games_and_drawings):
    bingo_games =[]
    bingo_game = []

    with open(games_and_drawings, "r", encoding="utf-8") as file:

        first_line = True

        for line in file:
            if first_line:
                drawings = [int(x.strip()) for x in line.split(',')]
                first_line = False

            elif line == "\n":
                first_bingo_line = True
                bingo_games.append(bingo_game)
            elif first_bingo_line:
                bingo_game = np.array(line.split())
                first_bingo_line = False
            else:
                bingo_game = np.vstack([bingo_game , np.array(line.split())])

    return np.asarray(bingo_games), drawings

if __name__ == "__main__":
    print(find_winning_bingo('day4/games.txt'))
