#!/usr/bin/env python3

from enum import Enum
import operator

class ConnectFour:

    def __init__(self, color="red"):
        self.player_color = color
        self.red_fire = '\U0001F525' #🔥
        self.blue_ice = '\U0001F9CA' #🧊
        self.rows = 6
        self.columns = 7
        self.grid = []
        self.Token = Enum('Token', 'RED BLUE')

    def init_moves_grid(self):
        """ Initialze empty multi-dim array.
        Arrays are columns, containing tokens placed in order, 0th is first.
        If the very first move was in column 1, the token would be in [0][0].
        """
        self.grid = [[None] * self.rows for col in range(self.columns)]

    def welcome_player(self):
        print('\n')
        print(f'Welcome! \nPlayer 1 (Red) is fire {self.red_fire} and Player 2',
            f'(Blue) is ice {self.blue_ice}.')
        print('The first to connect 4 tokens of their color wins.')
        print('Enter a column # (1-7) to drop your token.')
        print('\n')
        self.print_board()

    def gameplay(self):
        moves_count = 0
        player_red_turn = True
        while True:
            token = self.Token.RED if player_red_turn else self.Token.BLUE
            player = '🔥1🔥' if player_red_turn else '🧊2🧊'
            # Get current player's move
            while True:
                c_input = input(f'Player {player}\'s move: ')
                block_for_token = -1
                col = int(c_input) if c_input and c_input.isdigit() else None
                if col is None or col < 1 or col > 7:
                    # Invalid: NaN
                    print('You must enter in a single digit between 1 and 7')
                else:
                    col -= 1 # Translate user's col 1 to board col 0
                    block_for_token = self.next_empty_block(col)
                    if block_for_token == -1:
                        # Invalid: Block unavailable
                        print('That column is already full. Try another!')
                    else:
                        # Valid move
                        moves_count += 1
                        player_red_turn = not player_red_turn
                        break # End current player's move
            self.grid[col][block_for_token] = token
            self.print_board()
            # Check for win
            did_win = self.connected_4_exists(col, block_for_token)
            if did_win:
                print('🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆')
                print(f' Congratulations Player {player}! You won!')
                print('🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆')
                break
            if moves_count >= self.columns * self.rows:
                print('All game spaces are filled. Game over!')
                break

    def next_empty_block(self, column):
        """Returns lowest empty block for given column or -1 if full
        Lists in grid are columns, starting from bottom left of game board
        Imagine a vertical board where tokens are stacked in each column
        """
        empty_block = -1
        tokens_in_col = len([t for t in self.grid[column] if t is not None])
        if tokens_in_col < self.rows:
            empty_block = tokens_in_col
        return empty_block

    def connected_4_exists(self, column, row):
        """Check if current player completed a streak of 4 in any direction"""
        token = self.grid[column][row]
        count = 0
        add = operator.add
        mul = operator.mul
        sub = operator.sub
        # Left
        if self.streak_of_four(column, sub, row, mul, token):
            return True
        # Right
        if self.streak_of_four(column, add, row, mul, token):
            return True
        # Down
        if self.streak_of_four(column, mul, row, sub, token):
            return True
        # Diagonal left down
        if self.streak_of_four(column, sub, row, sub, token):
            return True
        # Diagonal right down
        if self.streak_of_four(column, add, row, sub, token):
            return True
        return False

    def streak_of_four(self, column, c_func, row, r_func, token):
        """Check for a streak of four in one direction matching given token"""
        is_streak = False
        for i in range(3):
            next_col = c_func(column, 1)
            next_row = r_func(row, 1)
            is_match = self.neighbor_block_matches(next_col, next_row, token)
            if not is_match:
                break
            if i == 2: # 3rd token checked besides original, aka 4 streak
                is_streak = True
                break
            column = next_col
            row = next_row

        return is_streak

    def neighbor_block_matches(self, column, row, token):
        """Check if a given neighbor block contains the desired token"""
        is_match = False
        if column >= 0 and column < self.columns and \
            row >= 0 and row < self.rows:
            if self.grid[column][row] == token:
                is_match = True
        return is_match

    def get_content_row(self, row):
        """Translate moves grid history into emoji visuals for printing board"""
        new_row = ''
        # Token Rows
        empty_block = '    '
        fire_block = ' 🔥 '
        ice_block = ' 🧊 '
        outer_wall = '||'
        inner_wall = '|'

        row_data = []
        for col in self.grid:
            row_data.append(col[row])

        new_row += outer_wall
        for d in row_data:
            if d is None:
                new_row += empty_block
            elif d == self.Token.BLUE:
                new_row += ice_block
            else:
                new_row += fire_block
            new_row += inner_wall
        new_row = new_row[:-1] # Removing last extraneous inner_wall
        new_row += outer_wall
        return new_row

    def print_board(self):
        """
           1    2    3    4    5    6    7
        ⟔------------------------------------
        || 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 ||
        ||----------------------------------||
        || 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 ||
        ||----------------------------------||
        || 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 ||
        ||----------------------------------||
        || 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 ||
        ||----------------------------------||
        || 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 ||
        ||----------------------------------||
        || 🔥 | 🧊 | 🔥 | 🧊 | 🔥 | 🧊 | 🔥 ||
        -------------------------------------⟓
        """
        board = ""
        # Divider Rows
        label_row = '   1    2    3    4    5    6    7   '
        top_row = '⟔------------------------------------'
        separator_row = '||----------------------------------||'
        bottom_row = '-------------------------------------⟓'
        board += label_row + '\n'
        board += top_row + '\n'
        # Content Rows
        for row in range(self.rows):
            reverse_counter = self.rows - (row+1)
            board += self.get_content_row(reverse_counter) + '\n'
            if row < self.rows-1:
                board += separator_row + '\n'
        board += bottom_row + '\n'
        print(board)

if __name__ == '__main__':
    game = ConnectFour()
    game.init_moves_grid()
    game.welcome_player()
    game.gameplay()
