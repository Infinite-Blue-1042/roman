import os, math
from roman import *
rootdir = os.path.dirname(os.path.dirname(__file__))
os.sys.path.insert(0, rootdir)


if __name__ == '__main__':
    robot = connect(use_sim=True)

    p1 = arm.Tool(-0.4, -0.4, 0.2, 0, math.pi, 0)

    p2 = arm.Joints(0, -math.pi/2, math.pi/2, -math.pi/2, -math.pi/2, 0)

    for i in range(3):
        robot.arm.move(p1, max_speed=1, max_acc=0.5)
        robot.arm.move(p2, max_speed=2, max_acc=2)
    
    robot.disconnect()
