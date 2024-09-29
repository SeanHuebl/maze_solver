# Maze Generation and Solver Project

## Overview

This project focuses on generating and solving mazes using Depth-First Search (DFS) algorithms. The maze is built using a grid-based system, with random wall-breaking to create solvable paths. The project also includes visual representations using `tkinter` to animate the maze generation and solving process. 

Unlike previous guided learning experiences, this project was highly independent and hands-off, with minimal pseudo code provided. This required deeper engagement with traversal algorithms and object-oriented programming (OOP) concepts.

## Deviation from Standard Conventions

In this project, you may notice a deviation from the common convention of representing grids with `i = row` and `j = column`. My mental model was oriented around `x` and `y` coordinates, where `x` represents width and `y` represents height. This felt intuitive to me while working with the maze as a grid. However, I recognize that in future projects, especially those involving matrices, it’s essential to align with the `i = row` and `j = column` standards, as it’s the typical convention in mathematical representations.

## Key Learnings

- **Type Hinting**: From the beginning of the project, I made a conscious effort to implement type hinting consistently across the codebase. This practice enhanced both code readability and maintainability, ensuring that the function signatures were clear and expectations for inputs and outputs were explicit.
  
- **Tkinter**: This project introduced me to using `tkinter` for visual representation and animation. Although the focus was on maze generation and traversal, learning to integrate `tkinter` added another layer of complexity to the project, especially in terms of real-time visualization.

- **Traversal Algorithms**: Working with Depth-First Search (DFS) for both maze generation and solving gave me greater confidence in traversal algorithms. The hands-on experience solidified my understanding of recursive algorithms, particularly how they can be applied to real-world grid-based problems like mazes.

- **Object-Oriented Programming (OOP)**: Designing the maze, cells, and window as classes helped reinforce my grasp of object-oriented programming principles. Each component of the maze was encapsulated in its own class, making the code modular and easier to maintain.

## Challenges and Growth

The project challenged me to solve complex problems without relying heavily on pre-provided solutions. This independence fostered a deeper learning experience, as I had to solve issues that arose during the development process on my own. In particular, my understanding of recursion, grid traversal, and the nuances of OOP improved significantly through this experience.

## Installation

To run this project, you will need to install a few dependencies. Below are the installation steps:

### Requirements
- Python 3.8+
- `tkinter` (for graphical display)
  
### Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone [<repository-url>](https://github.com/SeanHuebl/maze_solver)
   cd maze_solver/
   ```

2. **Install Dependencies**:
   Most of the project relies on standard libraries, but you’ll need to ensure `tkinter` is installed. If you don't have it installed, you can use the following commands depending on your operating system.

   - **Ubuntu/Debian**:
     ```bash
     sudo apt-get install python3-tk
     ```

   - **Windows**:
     `tkinter` should be installed automatically with Python on Windows, but if not, you can reinstall Python with the "tcl/tk and IDLE" checkbox selected.

   - **macOS**:
     `tkinter` is included with Python on macOS as well. If you face issues, you can try:
     ```bash
     brew install python-tk
     ```

3. **Run the Program**:
   You can run the maze generation program by executing the following:
   ```bash
   python3 main.py
   ```

## Running the Tests

To run the unit tests for this project, use:

```bash
python3 -m unittest discover
```
