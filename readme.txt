Vuong Khuat & Minh Vo
CS365 - AI & Machine Learning
Lab A
readme.txt

To run the program, you must use exactly two command line arguments.
The first argument should be the python file: vdkhuat16_mbvo14_main.py.

The second argument should be one of the followings:
    a) all_files_and_algorithms: to run the program with all 6 input files and all of the search algorithms.
    
    python vdkhuat16_mbvo14_main.py all_files_and_algorithms
    or
    python3 vdkhuat16_mbvo14_main.py all_files_and_algorithms (for systems that also have python 2.x)
    
    If you are running this on home.cs.earlham.edu, you will not need to worry about python or python3,
    just go with: 
    python vdkhuat16_mbvo14_main.py all_files_and_algorithms
    
    b) One of the files:
        - 1prize-medium.txt
        - 1prize-large.txt
        - 1prize-open.txt
        - multiprize-tiny.txt
        - multiprize-small.txt
        - multiprize-medium.txt
    
    
    python vdkhuat16_mbvo14_main.py FILE_NAME
    or
    python3 vdkhuat16_mbvo14_main.py FILE_NAME (for system that also has python 2.x)
    
    Example:
    python vdkhuat16_mbvo14_main.py 1prize-medium.txt
    
        If your second argument is one of the files with 1 prize, the program will ask you 
        to choose the algorithm to find the solution (by entering one of the numbers):
            1. Breadth-first search
            2. Depth-first search
            3. Greedy best-first search
            4. A* search
            
        If your second argument is one of the files with multiple prizes, the program will just run
        as there is only one algorithm to solve this type of maze: multi_astar.

If you fail to do any of the above (use exactly 2 arguments, have vdkhuat16_mbvo14_main.py as 
the first argument, have either all_files_and_algorithms or one of the six file names as the second 
argument, select one of the 4 numbers for the algorithms), the program will print out error messages
to suggest the error you are making and tell you to look back at this readme.txt file for more details.

The program will append the results to the output.txt file instead of overwriting the contents in that file.