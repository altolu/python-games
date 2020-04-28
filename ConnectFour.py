#!/usr/bin/env python3


class ConnectFour:

    def __init__(self, color="red"):
        self.player_color = color
        self.red_fire = '\U0001F525' #🔥
        self.blue_ice = '\U0001F9CA' #🧊
        self.rows = 6
        self.columns = 7
        self.grid = []

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
        col = 0
        player_red_turn = True

        while True:

            token = "RF" if player_red_turn else "BI"
            player = '1\'s 🔥' if player_red_turn else '2\'s 🧊'
            # Get current player's move
            while True:
                c_input = input(f'Player {player} move: ')
                col = int(c_input) if c_input and c_input.isdigit() else None
                if col is None or col < 1 or col > 7:
                    print('You must enter in a single digit between 1 and 7')
                else:
                    player_red_turn = not player_red_turn
                    break # End current player's move
            col -= 1 # Translate user's col 1 to board col 0
            col_of_grid = self.grid[col]
            tokens_in_col = len([t for t in col_of_grid if t is not None])
            self.grid[col][tokens_in_col] = token
            self.print_board()

            #TODO break when no more empty blocks

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
            elif d == 'BI':
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
