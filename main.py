

def delta_pose(drive_width, left_velocity, right_velocity, time_step):
    ''' calculate  dx, dy, and d_theta of how the robot will change pose '''

    # Calculate how far the left wheels move and right wheels move

    # use that calculate the turn radius

    # use the turn radius to calculate the turn angle. How does the turn angle connect to the d_theta.

    # create a triangle that you can use to calculate the dx and dy.

    return dx, dy, d_theta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    delta_pose(30, 5, 6, .02)
    delta_pose(30, 3, 8, .02)
    delta_pose(30, 7, 9, .02)

