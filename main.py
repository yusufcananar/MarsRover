"""
Code Review: Mars Rover
Part 1
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is
curiously rectangular, must be navigated by the rovers so that their on board cameras can get a
complete view of the surrounding terrain to send back to Earth.
A rover's position and location is represented by a combination of x and y co-ordinates and a letter
representing one of the four cardinal compass points. The plateau is divided up into a grid to
simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom
left corner and facing North.
In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and
'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its
current spot. 'M' means move forward one grid point, and maintain the same heading.
Assume that the square directly North from (x, y) is (x, y+1).
Input:
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are
assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover
has two lines of input. The first line gives the rover's position, and the second line is a series of
instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x
and y co-ordinates and the rover's orientation.
Each rover will be finished sequentially, which means that the second rover won't start to move
until the first one has finished moving.
Output:
The output for each rover should be its final co-ordinates and heading.
Input and Output
Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
Expected Output:
1 3 N
5 1 E
"""

# Constants
compass      = ['N', 'E', 'S', 'W']  # clock-wise order
instructions = ['M', 'L', 'R'] # movement keys


def commander(command, rover_position, upper_right_cords):
    """A function of decoding process of command keys into coordinates and heading information"""

    heading_index = compass.index(rover_position[2])
    commandList = list(command)

    for com in commandList:

        if com not in instructions:
            print("Use correct commands (M, L, R).")
            break

        if (rover_position[0]) < 0 or (rover_position[0] > upper_right_cords[0]) or (rover_position[1]) < 0 or (rover_position[1] > upper_right_cords[1]):
            print("Rover cannot move out of the plateau boundaries.")
            return ""

        if com == instructions[0]: # M

            #Advance in direction of
            if rover_position[2] == compass[1]:   # E
                rover_position[0] += 1

            elif rover_position[2] == compass[3]: # W
                rover_position[0] -= 1

            elif rover_position[2] == compass[0]: # N
                rover_position[1] += 1

            elif rover_position[2] == compass[2]: # S
                rover_position[1] -= 1

        elif com == instructions[1]: # L
            heading_index -= 1

        elif com == instructions[2]: # R
            heading_index += 1

        heading_index %= 4
        rover_position[2] = compass[heading_index] # heading

    rover_position[0] = str(rover_position[0]) # x
    rover_position[1] = str(rover_position[1]) # y

    return " ".join(rover_position)


def main():
    """MarsRover Main"""

    #Initial conditions
    lower_left_cords = (0, 0)
    upper_right_cords = (0, 0)
    isPlateauDefined = False

    # Plateau area decision loop
    while not isPlateauDefined:

        # Plateau of nxm
        try:
            n, m = input("Please enter the upper-right coordinates of the plateau : ").split()
            upper_right_cords = (int(n), int(m))
        except ValueError:
            print("Please enter only positive integers.")
            continue

        if upper_right_cords[0] <= 0 or upper_right_cords[1] <= 0:
            print("Plateau coordinates cannot be negative!")
            isPlateauDefined = False

        else:
            isPlateauDefined = True

    # Rover starting and commanding loop
    while isPlateauDefined:

        print("-"*50)
        # Rover's current position and heading
        try:
            x, y, heading = input("Please enter the rover's position : ").split()
            rover_position = [int(x), int(y), heading]

        except ValueError:
            print(f'Expected 3 values in the order of (x, y, direction).')
            continue

        if heading not in compass:
            print(f'Direction {heading} does not exists.')
            continue

        if rover_position[0] > upper_right_cords[0]:
            print('Rovers can\'t be out of plateau limits.')
            continue

        elif rover_position[1] > upper_right_cords[1]:
            print('Rovers can\'t be out of plateau limits.')
            continue

        elif rover_position[0] < lower_left_cords[0]:
            print('Rovers can\'t be out of plateau limits.')
            continue

        elif rover_position[1] < lower_left_cords[1]:
            print('Rovers can\'t be out of plateau limits.')
            continue

        # a series of instructions telling the rover how to explore the plateau
        command = input("Please enter the commands (M, L, R) : ")

        curr_rover_pos = commander(command, rover_position, upper_right_cords)
        print(curr_rover_pos)

        isMissionDead = input(" Entry : \n -1 : To End the Mission, \n  anything else : To Keep Sending the Rovers : ")

        if isMissionDead == '-1':
            print("Ending the Mission!")
            break


if __name__ == '__main__':
    main()

