from simulator import robot, FORWARD, BACKWARD, STOP
import random
# TODO: Write your code here!
#robot moves at 6 centimeters per second

def draw_circle_right(foc):
    "This function draws a circle to the right"
    howmany = int(input("How many circles would you like to draw"))
    for i in range(int(150 * howmany * foc)):
        left_sensor = robot.left_sonar()
        right_sensor = robot.right_sonar()
        if left_sensor > 10 and right_sensor > 10:
            robot.motors(left = FORWARD, right = FORWARD, seconds = 0.5)
            robot.motors(left = BACKWARD, right = FORWARD, seconds = 1)
        else:
            print("stop bruh")
            robot.motors(BACKWARD, BACKWARD, 3)
            break
def draw_square():
    "This function draws a perfect square"
    for i in range(4):
        left_sensor = robot.left_sonar()
        right_sensor = robot.right_sonar()
        if left_sensor > 32 and right_sensor > 32:
            robot.motors(FORWARD, FORWARD, 5)
            robot.motors(FORWARD, BACKWARD, 1.525)
        else:
            print("I AM TOO CLOSE. STOP ME")
            robot.motors(BACKWARD, BACKWARD, 3)
            break


# def go_random():
#     for i in range(50):
#         random.randint(1,50)
def dvd():
    "This function makes the robot go in a dvd-logo like motion around the box without touching or hitting the walls or corners"
    robot.motors(FORWARD, BACKWARD, 1)
    while True:
        for i in range(5):
            left_sensor = robot.left_sonar()
            right_sensor = robot.right_sonar()
            if left_sensor < right_sensor:
                robot.motors(FORWARD, FORWARD, (left_sensor/6)-1)
                robot.motors(BACKWARD, FORWARD, 2)
            elif right_sensor < left_sensor:
                robot.motors(FORWARD, FORWARD, (right_sensor/6)-1)
                robot.motors(FORWARD, BACKWARD, 2)
            elif left_sensor == right_sensor:
                robot.motors(BACKWARD, BACKWARD, 1.2)
                robot.motors(FORWARD, BACKWARD, 0.9)
    question()



def keos():
    "This is the menu that will pop up when you run the code and you contol what you want robot tot do"
    user_choice = input("Select a choice: Square, Circle, DVD, Half Circle")
    if user_choice == "Circle":
        draw_circle_right(1)
    elif user_choice == "Square":
        draw_square()
    elif user_choice == "DVD":
        dvd()
    elif user_choice == "Half Circle":
        draw_circle_right(0.5)


def question():
    response = int(input("Would you like to 1. Continue  2. Stop and go back to menu  3. Quit"))
    if response == 1:
      dvd()
    if response == 2:
      keos()
    if response == 3:
       quit

keos()

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