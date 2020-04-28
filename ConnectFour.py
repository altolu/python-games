#!/usr/bin/env python3


class ConnectFour:

    def __init__(self, color="red"):
        self.player_color = color
        self.red_fire = '\U0001F525' #🔥
        self.blue_ice = '\U0001F9CA' #🧊
        #pieces_on_board = [[], []]

    def welcome_player(self):
        c = 'blue'
        print('\n')
        print('Welcome Player 1! You are color {0}.'.format(self.player_color))
        print(f'Red is fire {self.red_fire} and Blue is ice {self.blue_ice}')
        print('\n')

    def print_board(self, rows=6, columns=7):
        board = ""
        # Divider Rows
        top_row = '⟔-------------------------------------'
        separator_row = '||----------------------------------||'
        bottom_row = '-------------------------------------⟓'
        # Token Rows
        empty_block = '    '
        fire_block = ' 🔥 '
        ice_block = ' 🧊 '
        outer_wall = '||'
        inner_wall = '|'
        temp_content_row = '||    |    |    |    |    |    |    ||'

        board += top_row + '\n'
        for row in range(rows):
            board += temp_content_row + '\n'
            if row < rows-1:
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
    game.welcome_player()
    game.print_board()
