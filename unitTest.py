import unittest
from main import *

class pyUnit(unittest.TestCase):

    def setUp(self):
        print("SET UP IS CALLED..")
        #Arrange
        self.x = 1
        self.y = 2
        self.heading = 'N'

        self.upper_right_cords = (5, 5)
        self.command = "LMLMLMLMM"
        self.rover_position = [self.x, self.y, self.heading]

        self.expected_result = "1 3 N"

    def tearDown(self):
        print("TEAR DOWN IS CALLED..")


    def test1_resulting_rover_position(self):

        print("TEST-SUITE-1 IS CALLED..")

        #Arrange
        self.x = 1
        self.y = 2
        self.heading = 'N'

        self.upper_right_cords = (5, 5)
        self.command = "LMLMLMLMM"
        self.rover_position = [self.x, self.y, self.heading]

        self.expected_result = "1 3 N"

        #Act
        result = commander(self.command, self.rover_position, self.upper_right_cords)

        #Assert
        self.assertEqual(result, self.expected_result)
        print("Test-1 result : ", result)

    def test2_resulting_rover_position(self):

        print("TEST-SUITE-2 IS CALLED..")

        #Arrange
        self.x = 3
        self.y = 3
        self.heading = 'E'

        self.upper_right_cords = (5, 5)
        self.command = "MMRMMRMRRM"
        self.rover_position = [self.x, self.y, self.heading]

        self.expected_result = "5 1 E"

        #Act
        result = commander(self.command, self.rover_position, self.upper_right_cords)

        #Assert
        self.assertEqual(result, self.expected_result)
        print("Test-2 result : ", result)

    def test3_resulting_rover_position(self):

        print("TEST-SUITE-3 IS CALLED..")

        #Arrange
        self.x = 2
        self.y = 0
        self.heading = 'S'

        self.upper_right_cords = (7, 3)
        self.command = "RMMRMMMRMMMMMMMLRR"
        self.rover_position = [self.x, self.y, self.heading]

        self.expected_result = "7 3 S"

        #Act
        result = commander(self.command, self.rover_position, self.upper_right_cords)

        #Assert
        self.assertEqual(result, self.expected_result)
        print("Test-3 result : ", result)

if __name__ == "__main__":
    unittest.main()