"""
- 2 human players, alternate turns
- 6X7 board
- disks start to fill up from bottom
- win if 4 consicutive disks ( row, col and diagonals)
- if all cells filled -> draw
- cant make a move on filled column
- invalid moves -> rejected

out of the scope:
- UI
- undo
- concerent game

Color ( Enum):
- blue
- red

State ( Enum):
    - not_started
    - in_progress
    - over

Disk
    - color: Color

User
    - name
    - Disk

board
    - nXm size board
    
    - display_board()
    - is_cell_empty(i, j)
    - is_index_valid(i, j)
    - get_value(i, j)
    - set_value(i, j)

GameManager
    - user_1, user2, board(6,7)
    - current_turn 
    - state
    - winner
    
    - get_current_turn()
    - swap_turn()
    - get_empty_row(col)
    - make_move(user, col)
    - update_game_status
    - get_state
    - get_winner()



"""
from enum import Enum

class COLOUR(Enum):
    RED = 'red'
    BLUE = 'blue'
    EMPTY = '0'

class STATE(Enum):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    OVER = 'over'

class Disk:
    def __init__(self, colour: COLOUR):
        self.colour = colour

    def get_color(self):
        return self.colour


class User:
    def __init__(self, name: str, disk: Disk):
        self.name = name
        self.disk = disk

class Board:
    def __init__(self, n: int, m: int):
        self.rows = n
        self.cols = m
        cols = [COLOUR.EMPTY.value for _ in range(m)]
        self.board = [cols for _ in range(n)]

    def is_index_valid(self, row: int, col: int)-> bool:
        if(row >=0 and row<=self.rows and col>=0 and col<=self.cols):
            return True
        return False

    def is_cell_empty(self, row:int, col: int)-> bool:
        if not self.is_index_valid(row, col) or self.board[row][col]!=COLOUR.EMPTY.value:
            return False
        return True

    def get_value(self, row: int, col: int):
        if not self.is_index_valid(row, col):
            return
        return self.board[row][col]

    def set_value(self, row: int, col: int, color: COLOUR):
        if not self.is_index_valid(row, col):
            return
        self.board[row][col]=color.value

    def is_board_filled(self):
        all_filled = True
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]==COLOUR.EMPTY.value:
                    all_filled=False
                    break
        return all_filled

    def display_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.board[i][j], end="")
            print()

class GameManager:
    def __init__(self, user_1: User, user_2: User):
        self.user_1 = user_1
        self.user_2 = user_2
        self.rows = 6
        self.cols = 7
        self.board = Board(self.rows, self.cols)
        self.state = STATE.NOT_STARTED.value
        self.winner = ""
        self.current_turn = user_1
        self.win_cutoff=4

    def get_current_turn(self):
        return self.current_turn

    def swap_current_turn(self):
        self.current_turn = self.user_1 if self.current_turn == self.user_2 else self.user_2

    def get_empty_row(self, col: int):
        index = -1
        for i in range(self.rows-1 , 0, -1):
            if self.board.get_value(i, col) == COLOUR.EMPTY.value:
                index = i
                break
        return index

    def update_state(self, state: STATE):
        self.state = state.value

    def get_state(self):
        return self.state

    def get_winner(self):
        return self.winner

    def display_winner(self):
        if self.winner:
            print(f"CONGOOO {self.winner} won the game")
        else:
            print("no winner yet")

    def _check_row(self, row: int, col: int):
        if col + self.win_cutoff - 1 <= self.cols-1:
            first_value = self.board[row][col]
            for j in range(col, col+self.win_cutoff):
                if self.board[row][j]==COLOUR.EMPTY.value:
                    return False
                if self.board[row][j]!=first_value:
                    return False
            return True
        return False

    def _check_col(self, row: int, col: int):
        if row + self.win_cutoff - 1 <= self.rows-1:
            first_value = self.board[row][col]
            for i in range(row, row+self.win_cutoff):
                if self.board[i][col]==COLOUR.EMPTY.value:
                    return False
                if self.board[i][col]!=first_value:
                    return False
            return True
        return False

    def _check_diagonal(self, row: int, col: int):
        if col + self.win_cutoff - 1 <= self.cols-1 and row + self.win_cutoff - 1 <= self.rows-1:
            first_value = self.board[row][col]
            for i in range(self.win_cutoff):
                current_value = self.board[row+i][col+i]
                if current_value == COLOUR.EMPTY.value:
                    return False
                if current_value!=first_value:
                    return False
            return True
        return False

    def check_winner(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self._check_col(i, j) or self._check_row(i, j) or self._check_diagonal(i, j):
                    self.winner = self.user_1 if self.board[i][j] == self.user_1.disk.get_color().value else self.user_2
                    self.update_state(STATE.OVER)
                    self.display_winner()
                    return
        
        

    def make_move(self, user: User, row: int, col: int):
        # - check if state is not over
        # 1. check if current user turn
        # 2. check if col is not out of range
        # 3. check if col is not filld
        # 4. update board
        # 5. swap turn
        # 6. check winner and display winner
        # 7. check board filled
        # - update game status

        if self.state==STATE.OVER or self.get_current_turn()!=user:
            return

        current_row_index = self.get_empty_row(col)

        if col<0 or col>=self.cols or current_row_index==-1:
            return

        self.board.set_value(current_row_index, col, user.disk.get_color())

        self.swap_current_turn()

        self.check_winner()

        if not self.get_winner() and self.board.is_board_filled():
            self.update_state(STATE.OVER)

        


    
        
