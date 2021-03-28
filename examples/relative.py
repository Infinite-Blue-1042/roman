import os, math, random, pybullet, scipy, numpy
from roman import *

rootdir = os.path.dirname(os.path.dirname(__file__))
os.sys.path.insert(0, rootdir)

def rand(max):
    return (random.random()-0.5)*max

if __name__ == '__main__':
    robot = connect(use_sim=True)
    
    t_step = 0.1
    r_step = 1
    for i in range(0, 5, 1):
        robot.move_simple(rand(t_step), rand(t_step), rand(t_step), rand(r_step), max_speed = 0.5)

    for i in range(0, 40, 1):
        robot.step(rand(t_step), rand(t_step), rand(t_step), rand(r_step), max_speed = 1, max_acc=1)

    robot.disconnect()
