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

        col = 0
        while True:
            col_selected = input('Player 1\'s column: ')
            col = int(col_selected) if col_selected and col_selected.isdigit() else None
            if col is None or col < 1 or col > 7:
                print('You must enter in a single digit between 1 and 7')
            else:
                # print(f'You selected {col}')
                break
        col -= 1
        self.grid[col][0] = 'RI'
        self.print_board()




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
