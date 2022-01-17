import numpy as np
import time
import math as m
import pygame
import random
from bin import rubiks
from bin import transform

class App:
    NUM_KEYS = [pygame.K_0,
                pygame.K_1,
                pygame.K_2,
                pygame.K_3,
                pygame.K_4,
                pygame.K_5,
                pygame.K_6,
                pygame.K_7,
                pygame.K_8,
                pygame.K_9]


    BORDER_COLORS = (0, 0, 0)
    MENU_COLOR = (50, 80, 50)

    R_CUBE = rubiks.Rubiks(dim=[3, 3, 3])

    angles = [m.pi / 6, m.pi / 3]
    sensitivity = [m.pi / 12, m.pi / 12]

    def __init__(self):
        self.running = True
        self._display_surf = None
        self.size = self.width, self.height = (800, 600)

        self.s_i = 0  # Slice Index

    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size)

        self.MOVES = [[self.R_CUBE.R,
                  self.R_CUBE.Rp,
                  self.R_CUBE.L,
                  self.R_CUBE.Lp],
                 [self.R_CUBE.F,
                  self.R_CUBE.Fp,
                  self.R_CUBE.B,
                  self.R_CUBE.Bp],
                 [self.R_CUBE.U,
                  self.R_CUBE.Up,
                  self.R_CUBE.D,
                  self.R_CUBE.Dp]]

        self.on_render()


        self.running = True

    def new_cube(self):
        self._display_surf.fill(App.MENU_COLOR)
        pygame.display.flip()

        new_dimensions = np.array([None, None, None])
        index = 0
        return_to_game = False
        while not return_to_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return_to_game = True
                        new_dimensions[0] = None
                        break
                    elif event.key == pygame.K_TAB:
                        index += 1
                        if index > 2:
                            index = 0
                    elif event.key == pygame.K_RETURN:
                        return_to_game = True
                    elif event.key in App.NUM_KEYS:
                        new_dimensions[index] = int(event.unicode)

        if not np.any(new_dimensions == None):
            self.R_CUBE = rubiks.Rubiks(new_dimensions)
            self.on_init()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.scramble_cube()
                elif event.key == pygame.K_RETURN:
                    self.new_cube()

            elif event.key in self.NUM_KEYS:
                self.s_i = int(event.unicode)

            elif event.mod & pygame.KMOD_SHIFT:
                if event.key == pygame.K_RIGHT:
                    self.angles[0] -= np.pi/2
                elif event.key == pygame.K_LEFT:
                    self.angles[0] += np.pi/2
                elif event.key == pygame.K_UP:
                    self.angles[1] += np.pi/2
                elif event.key == pygame.K_DOWN:
                    self.angles[1] -= np.pi/2

                if event.key == pygame.K_r:
                    self.R_CUBE.Rp(self.s_i)
                elif event.key == pygame.K_u:
                    self.R_CUBE.Up(self.s_i)
                elif event.key == pygame.K_f:
                    self.R_CUBE.Fp(self.s_i)
                elif event.key == pygame.K_l:
                    self.R_CUBE.Lp(self.s_i)
                elif event.key == pygame.K_d:
                    self.R_CUBE.Dp(self.s_i)
                elif event.key == pygame.K_b:
                    self.R_CUBE.Bp(self.s_i)
                

            else:
                if event.key == pygame.K_RIGHT:
                    self.angles[0] -= self.sensitivity[0]
                elif event.key == pygame.K_LEFT:
                    self.angles[0] += self.sensitivity[0]
                elif event.key == pygame.K_UP:
                    self.angles[1] += self.sensitivity[1]
                elif event.key == pygame.K_DOWN:
                    self.angles[1] -= self.sensitivity[1]

                elif event.key == pygame.K_r:
                    self.R_CUBE.R(self.s_i)
                elif event.key == pygame.K_u:
                    self.R_CUBE.U(self.s_i)
                elif event.key == pygame.K_f:
                    self.R_CUBE.F(self.s_i)
                elif event.key == pygame.K_l:
                    self.R_CUBE.L(self.s_i)
                elif event.key == pygame.K_d:
                    self.R_CUBE.D(self.s_i)
                elif event.key == pygame.K_b:
                    self.R_CUBE.B(self.s_i)

        elif event.type == pygame.MOUSEWHEEL:
            increment = 2*np.pi/20
            axis = min(1, pygame.key.get_mods())
            self.angles[axis] += -1*event.y*increment

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                increment = 2*np.pi/400
                self.angles[0] -= event.rel[0]*increment
                self.angles[1] -= event.rel[1]*increment

        elif event.type == pygame.MOUSEBUTTONDOWN:
            face = self.get_face(event.pos) 
            if np.sum(face) != 0:
                axis = np.where(face != 0)[0]
                direction = np.sum(face)
                if pygame.mouse.get_pressed()[0]:
                    if axis == 0:
                        if direction > 0:
                            self.R_CUBE.R(0)
                        else:
                            self.R_CUBE.L(0)
                    elif axis == 1:
                        if direction > 0:
                            self.R_CUBE.F(0)
                        else:
                            self.R_CUBE.B(0)
                    elif axis == 2:
                        if direction > 0:
                            self.R_CUBE.U(0)
                        else:
                            self.R_CUBE.D(0)

                elif pygame.mouse.get_pressed()[2]:
                    if axis == 0:
                        if direction > 0:
                            self.R_CUBE.Rp(0)
                        else:
                            self.R_CUBE.Lp(0)
                    elif axis == 1:
                        if direction > 0:
                            self.R_CUBE.Fp(0)
                        else:
                            self.R_CUBE.Bp(0)
                    elif axis == 2:
                        if direction > 0:
                            self.R_CUBE.Up(0)
                        else:
                            self.R_CUBE.Dp(0)

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.display_cube()
        pygame.display.flip()

    def display_cube(self):
        center = (400, 300)
        axes_2display = self.get_visible_axes(self.angles)
        th1, th2 = self.angles
        for a in axes_2display:
            if not (a==0).all():
                axis = np.where(a!=0)[0][0]
                d = sum(a)
                for wf in self.R_CUBE.get_face(axis, d):
                    corners = wf.get_face(axis, d)
                    corners = corners[[0, 1, 3, 2]]
                    corners = transform.project_2d(corners, th1, th2) + np.array(center).reshape((1, 2, 1))
                    corners_tup = []
                    for c in corners:
                        corners_tup.append((c[0][0], c[1][0]))

                    color = wf.colors[axis]
                    if not color == None:
                        self.draw_polygon(corners_tup, color, borders=8, border_color=self.BORDER_COLORS)

    def get_visible_axes(self, angles = None):
        if angles == None:
            angles = self.angles
        th1, th2 = angles
        axes = np.array([[1, 0, 0], [-1, 0, 0],
                         [0, 1, 0], [0, -1, 0],
                         [0, 0, 1], [0, 0, -1]])
        axes_2d = np.round(np.sum(axes*[m.sin(th2)*m.sin(th1), m.sin(th2)*m.cos(th1), m.cos(th2)], axis=1), 2)

        return axes[(axes_2d > 0)]

    def draw_wireframe(self, wf, center=(400, 300), angles=None, borders=2, filled = False):
        if angles == None:
            angles = self.angles
        th1, th2 = angles
        axes_2display = self.get_visible_axes(angles)


        for a in axes_2display:
            if not (a==0).all():
                axis = np.where(a!=0)[0][0]
                direction =sum(a)
                corners = wf.get_face(axis, direction)
                corners = corners[[0, 1, 3, 2]]
                corners = transform.project_2d(corners, th1, th2) + np.array(center).reshape((1, 2, 1))
                corners_tup = []
                for c in corners:
                    corners_tup.append((c[0][0], c[1][0]))

                if filled:
                    if direction == -1:
                        color = rubiks.colors[axis + 3]
                    else:
                        color = rubiks.colors[axis]
                    border_color = (0, 0, 0)
                else:
                    color = None
                    border_color = (200, 200, 200)

                self.draw_polygon(corners_tup, color, borders=borders, border_color=border_color) 

    def get_face(self, coordinates, center = (400, 300)):
        x, y = coordinates
        visible_axes = self.get_visible_axes()
        for axis in range(len(visible_axes)):
            direction = visible_axes[axis][axis]

            face_corners = transform.project_2d(self.R_CUBE.get_face_corners(axis, direction), self.angles[0], self.angles[1])  + np.array(center).reshape((1, 2, 1))
            face_corners = face_corners[[0, 1, 3, 2]]

            corners_tup = [(c[0][0], c[1][0]) for c in face_corners]
            if self.coordinates_in_polygon(coordinates, face_corners):
                return visible_axes[axis]

        return [0, 0, 0]

    def coordinates_in_polygon(self, coordinates, corners):
        th = 0
        for i in range(4):
            j = (i + 1)%4
            AB = np.array([coordinates[0] - corners[i][0], coordinates[1] - corners[i][1]]).flatten()
            AC = np.array([coordinates[0] - corners[j][0], coordinates[1] - corners[j][1]]).flatten()
            th += m.acos(np.dot(AB, AC)/(np.linalg.norm(AB)*np.linalg.norm(AC)))

        if abs(th - 2*np.pi) < 0.01:
            return True
        else:
            return False
    

    def draw_polygon(self, corners, color = None, borders=2, border_color=(255,255,255)):
        if borders != 0:
            pygame.draw.polygon(self._display_surf, border_color, corners, width=borders)
        if color != None:
            pygame.draw.polygon(self._display_surf, color, corners)

    def on_execute(self):
        pygame.init()
        if self.on_init() == False:
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_cleanup(self):
        pygame.display.quit()
        pygame.quit()

    def scramble_cube(self, n=None):
        if n is None:
            n = max([np.prod(self.R_CUBE.dim)//2, 100])

        for _ in range(n):
            axis = random.randint(0, 2)

            depth = random.randint(0, self.R_CUBE.dim[axis]-1)
            if depth == (self.R_CUBE.dim[axis]-1)/2:
                if random.randint(0, 2) == 1:
                    depth += 1
                else:
                    depth -= 1

            face = random.randint(0, len(self.MOVES[axis])-1)

            self.MOVES[axis][face](depth)


if __name__ == '__main__':
   app = App()
   app.on_execute()
