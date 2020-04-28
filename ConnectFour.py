#!/usr/bin/env python3


class ConnectFour:

    def __init__(self, color="red"):
        self.player_color = color
        self.red_fire = '\U0001F525' #🔥
        self.blue_ice = '\U0001F9CA' #🧊
        self.rows = 6
        self.columns = 7
        self.grid = []
        #pieces_on_board = [[], []]

    def init_pieces_array(self):
        counter = 0
        for _ in range(self.columns):
            new_col = [counter+num for num in range(1, self.rows+1)]
            counter += self.rows
            self.grid.append(new_col)

    def welcome_player(self):
        c = 'blue'
        print('\n')
        print('Welcome Player 1! You are color {0}.'.format(self.player_color))
        print(f'Red is fire {self.red_fire} and Blue is ice {self.blue_ice}')
        print('\n')


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
            datum = col[row]
            if datum is None:
                row_data.append(None)
            elif datum%2==0:
                row_data.append('BI')
            else:
                row_data.append('RF')

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
        top_row = '⟔-------------------------------------'
        separator_row = '||----------------------------------||'
        bottom_row = '-------------------------------------⟓'

        temp_content_row = '||    |    |    |    |    |    |    ||'

        board += top_row + '\n'
        for row in range(self.rows):
            # board += temp_content_row + '\n'
            reverse_counter = self.rows - (row+1)
            board += self.get_content_row(reverse_counter) + '\n'
            if row < self.rows-1:
                board += separator_row + '\n'
        board += bottom_row + '\n'

        print(board)



        # print('\n' + """
        # ⟔-------------------------------------
        # || 🔥 | 🔥 | 🔥 | 🔥 | 🔥 | 🔥 | 🔥 ||
        # ||----------------------------------||
        # || 🧊 | 🧊 | 🧊 | 🧊 | 🧊 | 🧊 | 🧊 ||
        # ||----------------------------------||
        # ||    | 🧊 | 🧊 | 🧊 | 🧊 | 🧊 | 🧊 ||
        # -------------------------------------⟓
        # """)




        # horizontal_div = '----' # plus 1 '-' above an inner wall
        # outer_wall = '||'
        # inner_wall = '|'
        # top_left_corner = '⟔-'
        # bottom_right_corner = '-⟓'
























if __name__ == '__main__':
    game = ConnectFour()
    game.init_pieces_array()
    print(f'Grid: {game.grid}')
    print('Removing some pieces...')
    game.grid[0][0] = None

    print(f'Grid: {game.grid}')
    game.welcome_player()
    game.print_board()
    game.init_pieces_array()
