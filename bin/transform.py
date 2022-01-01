import numpy as np
import math as m

def transform_2d(coordinates, th1, th2):
    n = len(coordinates)

    coordinates = np.array(coordinates).reshape((n, 3, 1))
    R1 = np.array([[m.cos(th1), -m.sin(th1), 0],
                   [m.sin(th1),  m.cos(th1), 0],
                   [         0,           0, 1]])
    
    R2 = np.array([[1,          0,           0],
                   [0, m.cos(th2), -m.sin(th2)],
                   [0, m.sin(th2),  m.cos(th2)]])
    
    results = np.zeros(coordinates.shape)
    for i in range(n):
        results[i] = np.linalg.multi_dot([R2, R1, coordinates[i]])

    return results


def project_2d(coordinates, th1, th2):
    P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    coordinates_2d = transform_2d(coordinates, th1, th2)
    
    results = np.zeros(coordinates_2d.shape)
    for i in range(len(results)):
        results[i] = np.linalg.multi_dot([P, coordinates_2d[i]])

    return results[:,0:2,:]

def isometric(coordinates):
    n = len(coordinates)
    coordinates = np.array(coordinates).reshape((n, 3, 1))
    R1 = np.array([[-np.sqrt(3), 0, np.sqrt(3)], [1, 2, 1], [np.sqrt(2), -np.sqrt(2), np.sqrt(2)]])
    R2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])

    results = np.zeros(coordinates.shape)
    for i in range(n):
        results[i] = np.linalg.multi_dot([R2, R1, coordinates[i]])/np.sqrt(6)

    return results[:,0:2,:]