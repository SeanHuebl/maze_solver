import unittest

from maze import Maze

class Tests(unittest.TestCase):
    """
    Unit test class for the Maze class. This class contains test cases 
    to verify the behavior of cell creation and the entrance/exit breaking.
    """

    def test_maze_create_cells(self) -> None:
        """
        Tests if the maze creates the correct number of rows and columns.
        """
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Assert that the number of columns is correct
        self.assertEqual(len(m1._cells), num_cols)

        # Assert that the number of rows in the first column is correct
        self.assertEqual(len(m1._cells[0]), num_rows)

        # Test again with different dimensions
        num_cols = 5
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)
    
    def test_break_entrance_and_exit(self) -> None:
        """
        Tests if the maze properly breaks the entrance and exit walls.
        """
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Break the entrance and exit and assert the walls are correctly removed.
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()
