from simulator import robot, FORWARD, BACKWARD, STOP
import random
# TODO: Write your code here!
#robot moves at 6 centimeters per second

def draw_circle_right():
    "This function draws a circle to the right"
    for i in range(30):
        robot.motors(left = FORWARD, right = FORWARD, seconds = 0.1)
        robot.motors(left = BACKWARD, right = FORWARD, seconds = 0.2)   
def draw_square():
    "This function draws a perfect square"
    for i in range(4):
        robot.motors(FORWARD, FORWARD, 5)
        robot.motors(FORWARD, BACKWARD, 1.525)
        
# def go_random():
#     for i in range(50):
#         random.randint(1,50)
def dvd(time):
    "This function makes the robot go in a dvd-logo like motion around the box without touching or hitting the walls or corners"
    robot.motors(FORWARD, BACKWARD, 1)
    while True:
        print(f"iteration #{i}")
        left_sensor = robot.left_sonar()
        right_sensor = robot.right_sonar()
        if left_sensor < right_sensor:
            robot.motors(FORWARD, FORWARD, (left_sensor/6)-1)
            robot.motors(BACKWARD, FORWARD, 2)
        else:
            robot.motors(FORWARD, FORWARD, (right_sensor/6)-1)
            robot.motors(FORWARD, BACKWARD, 2)




draw_circle_right()
draw_square()
dvd(5000)




user_choice = input("Select a choice: Square, Circle, DVD")
if user_choice == "Circle":
    draw_circle_right()
elif user_choice == "Square":
    draw_square()
elif user_choice == "DVD":
    dvd(5000)














# print(robot.left_sonar())  <- this all tests how fast the robot is in centimeters per second
# print(robot.right_sonar())

# robot.motors(FORWARD, FORWARD, 1)

# print(robot.left_sonar())
# print(robot.right_sonar())




# 6 centimeters per second/ CPS










# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
robot.exit()