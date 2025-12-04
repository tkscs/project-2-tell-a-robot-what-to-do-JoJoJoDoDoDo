from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!


for i in range(100):
    robot.motors(left = FORWARD, right = BACKWARD, seconds = 0.09)
    robot.motors(left = FORWARD, right = FORWARD, seconds = 0.26)




























# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
robot.exit()