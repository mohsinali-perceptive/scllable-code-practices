"""
- 3X3 grid
- player turn spaces on the grid with 'X' or 'O'
- players play alternatively
- win of player get his mark in rows, column or diagonal
- if grid filled without winner -> draw

- 2 human players
- move validations to make sure not wrong moves are made
- detection of win or draw scenarios


Symbol(Enum):
    - X
    - O
    - EMPTY

PlayerType(Enum):
    - HUMAN


Cell:
    - symbol

    = get_symbol(): Sumbol
    = set_symbol(): bool
    = is_empty(): bool

Board:
    - size
    - grid: Cell[size][size]

    = get_cell(row, col) -> Cell
    = is_valid_position(row, col)-> bool
    = is_empty(row, col) -> bool
    = is_full() -> bool
    = place_symbol(row, col, symbol): -> bool

Player:
    - name
    - symbol: Symbol
    - type: 'Human'

GameStatus:
    - IN_PROGRESS
    - NOT_STARTED
    - DRAW
    - WON

Game:
    - board : initialize borad 3X3
    - game_status: GameStatus
    - current_player: Player
    - player_1: Player
    - player_2: Player
    - winner: Player

    = make_move(player, row, col) -> bool
        - validate_player_move(player) -> bool
        - is_valid_position(row, col) -> bool
        - validate_empty_cell(row, col) -> bool
        - place_symbol(row, col, symbol) -> bool
        - check_winner()
        - get_status()
        - switch_turn()
    
    = validate_player_move(player) -> bool
    = validate_empty_cell(row, col) -> bool
    = swith_turn()
    = is_game_over() -> bool
    = get_winner() -> Player/None
    = show_results() -> None
    = get_current_player() -> Player
    = check_winner() # this will check for winner and set winner
    = get_status()
    = get_winner()

"""
from enum import Enum
class Symbol(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '


class Cell:
    def __init_(self):
        self.symbol = Symbol.EMPTY.value
    
    def get_symbol(self):
        return self.symbol
    
    def set_symbol(self, symbol: Symbol):
        self.symbol = Symbol[symbol].value
    
    def is_empty(self):
        return self.symbol == Symbol.EMPTY.value

class Player:
    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self, size: int):
        col = [Cell() for _ in range(size)]
        self.board = [col for _ in range(size)]
        self.size = size

    
    def get_value(self,row, col):
        return self.board[row][col].get_symbol()
    
    def is_valid_position(self, row, col):
        if row>=0 and row<self.size and col>0 and col < self.size:
            return True
        return False
    
    def set_value(self, row, col, symbol: Symbol):
        if self.is_valid_position(row, col):
            self.board[row][col].set_symbol(symbol)
    
    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.get_value(row, col), end=" ")
            print(" ")

board = Board(3)
board.set_value(1,2,Symbol.O.value)
board.print_board()


