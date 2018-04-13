# Vuong Khuat & Minh Vo
# CS365 - AI & Machine Learning
# Lab A
# vdkhuat16_mbvo14_main.py

from vdkhuat16_mbvo14_maze import Maze
from queue import *
from vdkhuat16_mbvo14_search_algorithms import *
import sys

def main():
    list_of_1prize_files = ["1prize-medium.txt", "1prize-large.txt", "1prize-open.txt"]
    list_of_multiprize_files = ["multiprize-tiny.txt", "multiprize-small.txt", "multiprize-medium.txt"]
    
    if len(sys.argv) == 2:
        # run the programs with all input files and search algorithms
        if sys.argv[-1] == "all_files_and_algorithms":
            for file in list_of_1prize_files:
                single_bfs(file)
                single_dfs(file)
                single_gbfs(file)
                single_astar(file)
            for file in list_of_multiprize_files:
                multi_astar(file)
        
        # run the program with an input file that has one prize
        elif sys.argv[-1] in list_of_1prize_files:
            file = sys.argv[-1]
            print("\nThe results of this program are going to be appended to the output.txt file.")
            print("Here are the single-prize search algorithms:\n")
            print("1. Breadth-first search;")
            print("2. Depth-first search;")
            print("3. Greedy best-first search;")
            print("4. A* search.\n")
            answer = input("Please enter the number to select the algorithm: ")      
            
            if answer == "1":
                single_bfs(file)
            elif answer == "2":
                single_dfs(file)
            elif answer == "3":
                single_gbfs(file)
            elif answer == "4":
                single_astar(file)
            else:
                print("The input is not one of the numbers above!")
            
        # run the program with an input file that has multiple prizes
        elif sys.argv[-1] in list_of_multiprize_files:
            file = sys.argv[-1]
            multi_astar(file)
            
        else:
            print("Error! Wrong argument!")
            print("Refer to the readme.txt file for more details about how to run the program.")
    
    else:
        print("Error! Please use exactly two arguments to run the program!")
        print("Refer to the readme.txt file for more details about how to run the program.")

if __name__ == "__main__":
    main()