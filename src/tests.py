import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Test if the number of columns matches the expected value
        self.assertEqual(len(m1._cells), num_cols)

        # Test if the number of rows in the first column matches the expected value
        self.assertEqual(len(m1._cells[0]), num_rows)
    
if __name__ == "__main__":
    unittest.main()