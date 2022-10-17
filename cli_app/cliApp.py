from bin import rubiks


class CliApp:
    EXIT_COMMANDS = ['Q', 'q', 'QUIT', 'Quit', 'quit']
    R_CUBE = rubiks.Rubiks(dim=[3, 3, 3])

    def __init__(self):
        self.running = True
        self.is_solved = False

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
        elif event == 'F':
            self.R_CUBE.F()
        elif event == 'Fp':
            self.R_CUBE.Fp()
        elif event == 'F2':
            self.R_CUBE.F()
            self.R_CUBE.F()
        # B moves
        elif event == 'B':
            self.R_CUBE.B()
        elif event == 'Bp':
            self.R_CUBE.Bp()
        elif event == 'B2':
            self.R_CUBE.B()
            self.R_CUBE.B()

    def on_execute(self):
        while self.running and not self.is_solved:
            next_move = input('Next Move: ')
            self.on_event(next_move)
            _, self.is_solved = self.get_cube()

        if self.is_solved:
            print('Congratulations!!!')
        else:
            print('Exiting the app.')

    def print_cube(self):
        for depth in [-1, 1]:
            for axis in [0, 1, 2]:
                print('Face no: ', axis + 3*(max(0, depth)))
                n = 0
                output = ''
                for _ in self.R_CUBE.get_face(axis, depth):
                    sticker_color = convert_color(_.colors[axis])
                    output += ' ' + sticker_color
                    n += 1
                    if n % 3 == 0:
                        print(output)
                        output = ''

    def get_cube(self):
        is_solved = True
        cube = []
        for depth in [-1, 1]:
            for axis in [0, 1, 2]:
                face_array = []
                for _ in self.R_CUBE.get_face(axis, depth):
                    sticker_color = convert_color(_.colors[axis])
                    if len(face_array) > 0 and sticker_color != face_array[-1]:
                        is_solved = False
                    face_array.append(sticker_color)
                cube.append(face_array)

        return cube, is_solved

# Static methods
def convert_color(color_tuple):
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
