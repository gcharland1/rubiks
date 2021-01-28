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


    def __init__(self, dim = (3, 3, 3), width = 300):
        self.dim = self.nx, self.ny, self.nz  = dim
        self.cube = np.zeros((dim), dtype='object')
        self.width = width
        self.piece_width = width/max(self.dim)

        self.initialize_cube()

    def initialize_cube(self):
        color = [None, None, None]
        for i in range(self.nx):
            x = (i-1)*self.piece_width
            if i-1 < 0:
                cx = self.colors[3]
            elif i-1 > 0:
                cx = self.colors[0]
            else:
                cx = None
            
            for j in range(self.ny):
                y = (j-1)*self.piece_width
                if j-1 < 0:
                    cy = self.colors[4]
                elif j-1 > 0:
                    cy = self.colors[1]
                else:
                    cy = None
                
                for k in range(self.nz):
                    z = (k-1)*self.piece_width
                    if k-1 < 0:
                        cz = self.colors[5]
                    elif k-1 > 0:
                        cz = self.colors[2]
                    else:
                        cz = None
                    
                    self.cube[i,j,k] = wireframe.Wireframe([x, y, z], self.piece_width, colors=[cx, cy, cz])

    def R(self):
        self.cube[2,:,:] = np.rot90(self.cube[2,:,:])
        x = 1*self.piece_width
        for j in range(3):
            y = (j-1)*self.piece_width
            for k in range(3):
                z = (k-1)*self.piece_width
                self.cube[2,j,k].change_position([x,y,z])
                self.cube[2,j,k].rotate(1, 2)

    def Rp(self):
        for i in range(3):
            self.R()

    def Lp(self):
        self.cube[0,:,:] = np.rot90(self.cube[0,:,:])
        x = -1*self.piece_width
        for j in range(3):
            y = (j-1)*self.piece_width
            for k in range(3):
                z = (k-1)*self.piece_width
                self.cube[0,j,k].change_position([x,y,z])
                self.cube[0,j,k].rotate(1, 2)

    def L(self):
        for i in range(3):
            self.Lp()

    def F(self):
        self.cube[:,2,:] = np.rot90(self.cube[:,2,:])
        y = 1*self.piece_width
        for i in range(3):
            x = (i-1)*self.piece_width
            for k in range(3):
                z = (k-1)*self.piece_width
                self.cube[i,2,k].change_position([x,y,z])
                self.cube[i,2,k].rotate(0, 2)

    def Fp(self):
        for i in range(3):
            self.F()

    def B(self):
        self.cube[:,0,:] = np.rot90(self.cube[:,0,:])
        y = -1*self.piece_width
        for i in range(3):
            x = (i-1)*self.piece_width
            for k in range(3):
                z = (k-1)*self.piece_width
                self.cube[i,0,k].change_position([x,y,z])
                self.cube[i,0,k].rotate(0, 2)

    def Bp(self):
        for i in range(3):
            self.B()

    def U(self):
        self.cube[:,:,2] = np.rot90(self.cube[:,:,2])
        z = 1*self.piece_width
        for i in range(3):
            x = (i-1)*self.piece_width
            for j in range(3):
                y = (j-1)*self.piece_width
                self.cube[i,j,2].change_position([x,y,z])
                self.cube[i,j,2].rotate(0, 1)

    def Up(self):
        for i in range(3):
            self.U()

    def Dp(self):
        self.cube[:,:,0] = np.rot90(self.cube[:,:,0])
        z = -1*self.piece_width
        for i in range(3):
            x = (i-1)*self.piece_width
            for j in range(3):
                y = (j-1)*self.piece_width
                self.cube[i,j,0].change_position([x,y,z])
                self.cube[i,j,0].rotate(0, 1)

    def D(self):
        for i in range(3):
            self.Dp()


    def get_face(self, axis=0, direction=1):
        d = direction + 1 # Index of np slice
        if axis == 0:
            pieces = self.cube[d,:,:]

        elif axis == 1:
            pieces = self.cube[:,d,:]

        elif axis == 2:
            pieces = self.cube[:,:,d]
        else:
            print('Unknown axis', axis)
            return np.array([])

        return pieces.ravel()

    def cli_display(self):
        print(self.state[0:3].center(9, ' '))
        print(self.state[3:6].center(9, ' '))
        print(self.state[6:9].center(9, ' '))
        print(self.state[9:21])
        print(self.state[21:33])
        print(self.state[33:45])
        print(self.state[45:48].center(9, ' '))
        print(self.state[48:51].center(9, ' '))
        print(self.state[51:54].center(9, ' '))

if __name__=='__main__':
    cube = Rubiks()
