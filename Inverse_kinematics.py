import math
import numpy as np

x = 4
y = 2
goal1 = [x, y]
arm_position = np.array([[0,0],[5.0,0],[10.0,0]])

#start with some coordinate that has a fixed angle (like [5,0], [10,0] will have 0 and 180) 
arm_angle = None

arm_length = [5,5]
reach = sum(arm_length)
longest = math.sqrt(x^2+y^2)


#algorithm for calculating the position from the goal to the origin
def reverse_calculation(p1,p2,mag):
    dir_vector = p1 - p2
    mag_of_difference = math.sqrt(dir_vector[0]**2+dir_vector[1]**2)
    unit_vector = np.divide(dir_vector,mag_of_difference)
    new_vector = unit_vector*mag
    new_coord = p2 + new_vector
    return new_coord

#algorithm for calculating the position going from origin to the goal
def forward_calculation(p1,p2,mag):
    dir_vector = p1 - p2
    mag_of_difference = math.sqrt(dir_vector[0]**2+dir_vector[1]**2)
    unit_vector = np.divide(dir_vector,mag_of_difference)
    new_vector = unit_vector*mag
    new_coord = p2 + new_vector
    return new_coord

#reaching the goal within the number of 
def coord_calc(goal, arm_pos, link_length):
    new_pos = arm_pos.copy()
    old_arm_pos = arm_pos.copy()
    actual_err_x = 1
    actual_err_y = 1
    allowed_err = 0.05

    while (actual_err_x >= allowed_err) or (actual_err_y >= allowed_err):
        #reverse
        for i in range(len(new_pos)-1,-1, -1):
            if i == len(new_pos)-1:
                new_pos[i] = goal
            else:
                new_pos[i] = reverse_calculation(new_pos[i],new_pos[i+1],link_length[i])
        #forward
        for i in range(len(new_pos)):
            if i == 0: 
                new_pos[0] = [0,0]
            else:
                new_pos[i] = forward_calculation(new_pos[i],new_pos[i-1],link_length[i-1])
        actual_err_x = abs((new_pos[-1][0] - goal[0]))/goal[0]
        actual_err_y = abs((new_pos[-1][1] - goal[1]))/goal[1]

    return new_pos, old_arm_pos

#finding the angle that needs to be rotated for each joint
def joint_angle(vector_a, vector_b):
    vec_a_mag = abs(math.sqrt(vector_a[0]**2 + vector_a[1]**2))
    vec_b_mag = abs(math.sqrt(vector_b[0]**2 + vector_b[1]**2))
    theta = math.acos(np.dot(vector_a, vector_b)/(vec_a_mag*vec_b_mag))
    # print(np.dot(vector_a, vector_b))
    return theta

def update_angle(arm_pos, old_arm_pos):
    theta1 = joint_angle(arm_pos[1],old_arm_pos[1])
    theta2 = 180 - joint_angle(old_arm_pos[1],old_arm_pos[2])
    a2prime = np.subtract(arm_pos[2],arm_pos[1])
    print(theta2)
    print(a2prime)
    print(arm_pos[1])

    #find angle between a1 and a2prime
    theta2prime = theta2 - 180 - joint_angle(arm_pos[1],a2prime)

    arm_angle = [theta1, theta2prime]
    for i,s in enumerate(arm_angle):
        arm_angle[i] = s*(180/math.pi)

    #this will return an array
    return arm_angle


#drawing a line from the given point to the given location
#p1 is start, p2 is goal
def draw_line(p1, p2, piece):
    path = []
    #different movements apply to different pieces?
    #rook: can move in a straight line. Just move straight to the point
    #bishop: move diagonal?
    #knight: must move between pieces
    #pawn: straight line 
    #king: straight line
    #queen: diagonal and straight line
    if piece == "knight":
        #if the destination is to the left of the board
        #move one unit left
        if p2[0] <= p1[0]:
            path = []
        else:
            path = []
        #if the destination is to the right of the board
        pass
    pass





new_pos,old_pos = coord_calc(goal1,arm_position, arm_length)
new_angles = update_angle(new_pos, old_pos)
print(new_angles)
