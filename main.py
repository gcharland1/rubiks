import numpy as np
import math as m
import pygame
import wireframe
import rubiks
import transform

class App:
    border_color = (0, 0, 0)
    def __init__(self):
        self.running = True
        self._display_surf = None
        self.size = self.width, self.height = (800, 600)

        self.wf = wireframe.Wireframe(width=100)
        self.r_cube = rubiks.Rubiks()
        self.angles = [m.pi/6, m.pi/6]

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._display_surf.fill((0, 0, 0))
        self.on_render()
        self.running = True
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_q:
                    self.running = False

            elif event.mod & pygame.KMOD_SHIFT:
                if event.key == pygame.K_r:
                    self.r_cube.Rp()
                    self.on_render()
                elif event.key == pygame.K_u:
                    self.r_cube.Up()
                    self.on_render()
                elif event.key == pygame.K_f:
                    self.r_cube.Fp()
                    self.on_render()
                elif event.key == pygame.K_l:
                    self.r_cube.Lp()
                    self.on_render()
                elif event.key == pygame.K_d:
                    self.r_cube.Dp()
                    self.on_render()
                elif event.key == pygame.K_b:
                    self.r_cube.Bp()
                    self.on_render()

            else:
                if event.key == pygame.K_RIGHT:
                    self.angles[0] -= m.pi/6
                    self.on_render()
                elif event.key == pygame.K_LEFT:
                    self.angles[0] += m.pi/6
                    self.on_render()
                elif event.key == pygame.K_UP:
                    self.angles[1] += m.pi/6
                    self.on_render()
                elif event.key == pygame.K_DOWN:
                    self.angles[1] -= m.pi/6
                    self.on_render()

                elif event.key == pygame.K_r:
                    self.r_cube.R()
                    self.on_render()
                elif event.key == pygame.K_u:
                    self.r_cube.U()
                    self.on_render()
                elif event.key == pygame.K_f:
                    self.r_cube.F()
                    self.on_render()
                elif event.key == pygame.K_l:
                    self.r_cube.L()
                    self.on_render()
                elif event.key == pygame.K_d:
                    self.r_cube.D()
                    self.on_render()
                elif event.key == pygame.K_b:
                    self.r_cube.B()
                    self.on_render()


    def on_loop(self):
        pass

    def on_render(self):
        axis = [1, 1, 1]
        self._display_surf.fill((0, 0, 0))
        self.display_cube()
        pygame.display.flip()

    def display_cube(self):
        center = (400, 300)
        axes_2display = self.get_visible_axes(self.angles)
        th1, th2 = self.angles
        for a in axes_2display:
            if (a==0).all():
                next
            else:
                axis = np.where(a!=0)[0][0]
                d = sum(a)
                direction = d*self.r_cube.piece_width
                for wf in self.r_cube.get_face(axis, d):
                    corners = wf.get_face(axis, d)
                    corners = corners[[0, 1, 3, 2]]
                    corners = transform.project_2d(corners, th1, th2) + np.array(center).reshape((1, 2, 1))
                    corners_tup = []
                    for c in corners:
                        corners_tup.append(tuple(c))

                    color = wf.colors[axis]
                    if not color == None:
                        self.draw_polygon(corners_tup, color, borders=8, border_color=self.border_color) 

    def get_visible_axes(self, angles = [m.pi/6, m.pi/6]):
        th1, th2 = angles
        axes = np.array([[1, 0, 0], [-1, 0, 0],
                         [0, 1, 0], [0, -1, 0],
                         [0, 0, 1], [0, 0, -1]])
        axes_2d = np.round(np.sum(axes*[m.sin(th2)*m.sin(th1), m.sin(th2)*m.cos(th1), m.cos(th2)], axis=1), 2)

        return axes[(axes_2d > 0)]
 
    def draw_wireframe(self, wf,  angles = [m.pi/6, m.pi/6], borders=2, filled = False):
        th1, th2 = angles
        axes_2display = self.get_visible_axes(angles)
        
        
        center = (400, 300)
        for a in axes_2display:
            if (a==0).all():
                next
            else:
                axis = np.where(a!=0)[0][0]
                direction =sum(a)
                corners = wf.get_face(axis, direction)
                corners = corners[[0, 1, 3, 2]]
                corners = transform.project_2d(corners, th1, th2) + np.array(center).reshape((1, 2, 1))
                corners_tup = []
                for c in corners:
                    corners_tup.append(tuple(c))

                if filled:
                    if direction == -1:
                        color = self.colors[axis + 3]
                    else:
                        color = self.colors[axis]
                    border_color = (0, 0, 0)
                else:
                    color = None
                    border_color = (200, 200, 200)

                self.draw_polygon(corners_tup, color, borders=borders, border_color=border_color) 
                

    def draw_polygon(self, corners, color = None, borders=2, border_color=(255,255,255)):
        if borders != 0:
            pygame.draw.polygon(self._display_surf, border_color, corners, width=borders)
        if color != None:
            pygame.draw.polygon(self._display_surf, color, corners)
        
    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            #self.on_render()

        self.on_cleanup()

    def on_cleanup(self):
        pygame.display.quit()
        pygame.quit()


if __name__ == '__main__':
   app = App()
   app.on_execute()
