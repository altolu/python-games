#!/usr/bin/env python3

from enum import Enum

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
        self.grid = [[None] * self.rows for col in range(self.columns)]

    def welcome_player(self):
        c = 'blue'
        print('\n')
        print(f'Welcome! \nPlayer 1 (Red) is fire {self.red_fire} and Player 2 (Blue) is ice {self.blue_ice}.')
        print('The first to connect 4 tokens of their color wins.')
        print('Enter a column # (1-7) to drop your token.')
        print('\n')
        self.print_board()

    def gameplay(self):
        moves_count = 0
        player_red_turn = True
        while True:
            token = self.Token.RED if player_red_turn else self.Token.BLUE
            player = '1\'s 🔥' if player_red_turn else '2\'s 🧊'
            # Get current player's move
            while True:
                c_input = input(f'Player {player} move: ')
                block_for_token = -1
                col = int(c_input) if c_input and c_input.isdigit() else None
                if col is None or col < 1 or col > 7:
                    print('You must enter in a single digit between 1 and 7')
                else:
                    col -= 1 # Translate user's col 1 to board col 0
                    block_for_token = self.next_empty_block(col)
                    if block_for_token == -1:
                        print('That column is already full. Try another!')
                    else:
                        moves_count += 1
                        player_red_turn = not player_red_turn
                        break # End current player's move
            self.grid[col][block_for_token] = token
            self.print_board()
            if moves_count >= self.columns * self.rows:
                print('All game spaces are filled. Game over!')
                break
            # TODO: break when no more empty blocks


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

    def get_content_row(self, row):
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
        board = ""
        # Divider Rows
        label_row = '   1    2    3    4    5    6    7   '
        top_row = '⟔------------------------------------'
        separator_row = '||----------------------------------||'
        bottom_row = '-------------------------------------⟓'

        board += label_row + '\n'
        board += top_row + '\n'
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
