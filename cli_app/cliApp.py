from bin import rubiks


class CliApp:
    EXIT_COMMANDS = ['Q', 'q', 'QUIT', 'Quit', 'quit']
    R_CUBE = rubiks.Rubiks(dim=[3, 3, 3])

    def __init__(self):
        self.running = False

    def convert_color(self, color_tuple):
        if color_tuple == (255, 0, 0):
            return 'R'
        elif color_tuple == (255, 126, 0):
            return 'O'
        elif color_tuple == (0, 0, 255):
            return 'B'
        elif color_tuple == (62, 225, 62):
            return 'G'
        elif color_tuple == (255, 255, 255):
            return 'W'
        elif color_tuple == (255, 255, 0):
            return 'Y'

        return '?'

    def on_event(self, event):
        if event in self.EXIT_COMMANDS:
            self.running = False
        # R moves
        elif event == 'R':
            self.R_CUBE.R()
        elif event == 'Rp':
            self.R_CUBE.Rp()
        elif event == 'R2':
            self.R_CUBE.R()
            self.R_CUBE.R()
        # L moves
        elif event == 'L':
            self.R_CUBE.L()
        elif event == 'Lp':
            self.R_CUBE.Lp()
        elif event == 'L2':
            self.R_CUBE.L()
            self.R_CUBE.L()
        # U moves
        elif event == 'U':
            self.R_CUBE.U()
        elif event == 'Up':
            self.R_CUBE.Up()
        elif event == 'U2':
            self.R_CUBE.U()
            self.R_CUBE.U()
        # D moves
        elif event == 'D':
            self.R_CUBE.D()
        elif event == 'Dp':
            self.R_CUBE.Dp()
        elif event == 'D2':
            self.R_CUBE.D()
            self.R_CUBE.D()
        # F moves
        elif event == 'L':
            self.R_CUBE.L()
        elif event == 'Lp':
            self.R_CUBE.Lp()
        elif event == 'L2':
            self.R_CUBE.L()
            self.R_CUBE.L()
        # B moves
        elif event == 'B':
            self.R_CUBE.B()
        elif event == 'Bp':
            self.R_CUBE.Bp()
        elif event == 'B2':
            self.R_CUBE.B()
            self.R_CUBE.B()

    def on_execute(self):
        self.running = True

        while self.running:
            next_move = input('Next Move: ')
            self.on_event(next_move)
            self.print_cube()

        print('Exiting the app.')

    def print_cube(self):
        for depth in [-1, 1]:
            for axis in [0, 1, 2]:
                print('Face no: ', axis + 3*(max(0, depth)))
                n = 0
                output = ''
                for wf in self.R_CUBE.get_face(axis, depth):
                    sticker_color = self.convert_color(wf.colors[axis])
                    output += ' ' + sticker_color
                    n += 1
                    if n % 3 == 0:
                        print(output)
                        output = ''
