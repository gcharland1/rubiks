import numpy as np

class Wireframe:
    _unit_corners = np.transpose(np.array([[1,  1,  1,  1, -1, -1, -1, -1], 
                                           [1,  1, -1, -1,  1,  1, -1, -1],
                                           [1, -1,  1, -1,  1, -1,  1, -1]]))

    def __init__(self, position=None, width = 50, colors=None):
        if position is None:
            position = [0, 0, 0]
        if colors is None:
            colors = [None, None, None]

        self.position = np.array(position)
        self.width = width
        self.colors = colors

        self.compute_corners()

    def compute_corners(self):
        self.corners = self.position + Wireframe._unit_corners * self.width/2 

    def get_face(self, axis = 0, direction = 1):
        cond = [0, 0, 0]
        cond[axis] = direction
        corners =  self.corners[(self._unit_corners==cond).any(axis=1)]
        return corners[np.argsort(corners[:,1]),:]

    def change_position(self, new_position):
        self.position = np.array(new_position)
        self.compute_corners()

    def rotate(self, ax1, ax2):
        self.colors[ax1], self.colors[ax2] = self.colors[ax2], self.colors[ax1]

    def get_edges(self, axis = 0):
        if axis == 0:
            a2 = 1
        elif axis == 1:
            a2 = 2
        elif axis == 2:
            a2 = 0
        else:
            axis = 0
            a2 = 1
            print("Axis out of boud, using 0")

        self.corners = self.corners[np.argsort(self.corners[:,a2]),:]
        self.corners = self.corners[np.argsort(self.corners[:,axis]),:]
        
        edges = np.zeros((4, 2, 3))
        for i in range(4):
            edges[i] = (self.corners[i,:], self.corners[i+4,:])

        return edges
