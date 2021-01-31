import numpy as np
import wireframe


class Rubiks:
    RED = (255, 0, 0)
    ORANGE = (255, 126, 0)
    BLUE = (0, 0, 255)
    GREEN = (62, 225, 62)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    colors = [RED, BLUE, YELLOW, ORANGE, GREEN, WHITE]

    def __init__(self, dim=None, width=300):
        if dim is None:
            dim = [3, 3, 3]
        self.dim = self.nx, self.ny, self.nz = dim
        self.cube = np.zeros((self.nx, self.ny, self.nz), dtype='object')
        self.width = width
        self.piece_width = width / max(self.dim)

        self.initialize_cube()

    def initialize_cube(self):

        for i in range(self.nx):
            if i == 0:
                cx = self.colors[3]
            elif i == self.nx - 1:
                cx = self.colors[0]
            else:
                cx = None

            for j in range(self.ny):
                if j == 0:
                    cy = self.colors[4]
                elif j == self.ny - 1:
                    cy = self.colors[1]
                else:
                    cy = None

                for k in range(self.nz):
                    if k == 0:
                        cz = self.colors[5]
                    elif k == self.nz - 1:
                        cz = self.colors[2]
                    else:
                        cz = None

                    position = self.compute_pieces_positions(i, j, k)
                    self.cube[i, j, k] = wireframe.Wireframe(position, self.piece_width, colors=[cx, cy, cz])

    def compute_pieces_positions(self, i, j, k):
        d_i = (self.nx - 1) / 2
        d_j = (self.ny - 1) / 2
        d_k = (self.nz - 1) / 2
        x = (i - d_i) * self.piece_width
        y = (j - d_j) * self.piece_width
        z = (k - d_k) * self.piece_width
        return [x, y, z]

    def R(self):
        i = self.nx - 1
        self.cube[i, :, :] = np.rot90(self.cube[i, :, :])
        for j in range(self.ny):
            for k in range(self.nz):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(1, 2)

    def Rp(self):
        for _ in range(3):
            self.R()

    def Lp(self):
        i = 0
        self.cube[i, :, :] = np.rot90(self.cube[i, :, :])
        for j in range(self.ny):
            for k in range(self.nz):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(1, 2)

    def L(self):
        for _ in range(3):
            self.Lp()

    def U(self):
        k = self.nz - 1
        self.cube[:, :, k] = np.rot90(self.cube[:, :, k])
        for i in range(self.nx):
            for j in range(self.ny):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(0, 1)

    def Up(self):
        for _ in range(3):
            self.U()

    def Dp(self):
        k = 0
        self.cube[:, :, k] = np.rot90(self.cube[:, :, k])
        for i in range(self.nx):
            for j in range(self.ny):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(0, 1)

    def D(self):
        for _ in range(3):
            self.Dp()

    def Fp(self):
        j = self.ny - 1
        self.cube[:, j, :] = np.rot90(self.cube[:, j, :])
        for i in range(self.nx):
            for k in range(self.nz):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(0, 2)

    def F(self):
        for _ in range(3):
            self.Fp()

    def B(self):
        j = 0
        self.cube[:, j, :] = np.rot90(self.cube[:, j, :])
        for i in range(self.nx):
            for k in range(self.nz):
                position = self.compute_pieces_positions(i, j, k)
                self.cube[i, j, k].change_position(position)
                self.cube[i, j, k].rotate(0, 2)

    def Bp(self):
        for _ in range(3):
            self.B()

    def get_face(self, axis=0, direction=1):
        if direction > 0:
            d = self.dim[axis] - 1
        else:
            d = 0
        if axis == 0:
            pieces = self.cube[d, :, :]

        elif axis == 1:
            pieces = self.cube[:, d, :]

        elif axis == 2:
            pieces = self.cube[:, :, d]
        else:
            print('Unknown axis', axis)
            return np.array([])

        return pieces.ravel()


if __name__ == '__main__':
    cube = Rubiks()
