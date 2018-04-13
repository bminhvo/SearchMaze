# Vuong Khuat & Minh Vo
# CS365 - AI & Machine Learning
# Lab A
# vdkhuat16_mbvo14_search_algorithms.py

from vdkhuat16_mbvo14_maze import Maze
from queue import Queue, PriorityQueue
import sys

def single_bfs(filename):
    """
    The function that uses Breadth-first search strategy 
    to find the path to the prize in the single-prize case.
    @param:
        filename: a file containing a maze.
    """
    maze = Maze(open(filename, 'r').read())
    
    frontier = Queue()
    
    # a separate list to keep track of states we add to the frontier
    # as we cannot look inside elements of a queue.
    frontier_tracker = []
    
    explored = []
    frontier.put(maze.get_initial_state())
    frontier_tracker.append(maze.get_initial_state())
    
    while not frontier.empty():
        state = frontier.get()
        explored.append(state)
        
        for neighbor in maze.moveable_nodes(state):
            if not has_visited(neighbor, explored) and not neighbor in frontier_tracker:
                if (neighbor.has_collected_all()): # goal is achieved.
                    display_solution(filename, "single_bfs", maze, neighbor, explored)
                    return
                frontier.put(neighbor)
                frontier_tracker.append(neighbor)
    print("Failed to collected all prizes.")
    
        
def single_dfs(filename):
    """
    The function that uses Depth-first search strategy 
    to find the path to the prize in the single-prize case.
    @param:
        filename: a file containing a maze.
    """
    maze = Maze(open(filename, 'r').read())
    
    frontier = []   # a list used as a stack
    
    # a separate list to keep track of states we add to the frontier
    # as we cannot look inside elements of a stack.
    frontier_tracker = []
    
    explored = []
    frontier.append(maze.get_initial_state())
    frontier_tracker.append(maze.get_initial_state())
    
    while frontier:
        state = frontier.pop()
        explored.append(state)
        
        for neighbor in maze.moveable_nodes(state):
            if not has_visited(neighbor, explored) and not neighbor in frontier_tracker:
                if (neighbor.has_collected_all()): # goal is achieved.
                    display_solution(filename, "single_dfs", maze, neighbor, explored)
                    return
                frontier.append(neighbor)
                frontier_tracker.append(neighbor)
    print("Failed to collected all prizes.")

def single_gbfs(filename):
    """
    The function that uses Greedy best-first search strategy 
    to find the path to the prize in the single-prize case.
    @param:
        filename: a file containing a maze.
    """
    maze = Maze(open(filename, 'r').read())
    
    frontier = PriorityQueue()
    
    # a separate list to keep track of states we add to the frontier
    # as we cannot look inside elements of a queue.
    frontier_tracker = []
    
    explored = []
    
    curr_pos = maze.get_initial_state()
    frontier_tracker.append(curr_pos)
    
    prize_location = next(iter(curr_pos.prizes_locations))
    
    # we use the Manhattan distance from the current position 
    # to the prize as our heuristic function.
    frontier.put((maze.manhattan_distance(curr_pos.id, prize_location),
            curr_pos))
    
    while not frontier.empty():
        state = frontier.get()[1]
        explored.append(state)
        
        for neighbor in maze.moveable_nodes(state):
            if not has_visited(neighbor, explored) and not neighbor in frontier_tracker:
                if (neighbor.has_collected_all()): # goal is achieved.
                    display_solution(filename, "single_gbfs", maze, neighbor, explored)
                    return
                frontier.put((maze.manhattan_distance(neighbor.id, prize_location),
                    neighbor))
                frontier_tracker.append(neighbor)
    print("Failed to collected all prizes.")

def single_astar(filename):
    """
    The function that uses A* search strategy 
    to find the path to the prize in the single-prize case.
    @param:
        filename: a file containing a maze.
    """
    maze = Maze(open(filename, 'r').read())
    
    frontier = PriorityQueue()
    
    # a separate list to keep track of states we add to the frontier
    # as we cannot look inside elements of a queue.
    frontier_tracker = []
    
    explored = []
    
    curr_pos = maze.get_initial_state()
    frontier_tracker.append(curr_pos)
    
    prize_location = next(iter(curr_pos.prizes_locations))
    
    # we use the Manhattan distance from the current position 
    # to the prize as our heuristic function.
    frontier.put((single_astar_cost(maze, curr_pos, prize_location),
            curr_pos))
    
    while not frontier.empty():
        state = frontier.get()[1]
        explored.append(state)
        
        for neighbor in maze.moveable_nodes(state):
            if not has_visited(neighbor, explored) and not neighbor in frontier_tracker:
                if (neighbor.has_collected_all()): # goal is achieved.
                    display_solution(filename, "single_astar", maze, neighbor, explored)
                    return
                frontier.put((single_astar_cost(maze, neighbor, prize_location),
                    neighbor))
                frontier_tracker.append(neighbor)
    print("Failed to collected all prizes.")

def multi_astar(filename):
    """
    The function that uses A* search strategy 
    to find the path to the prizes in the multi-prize case.
    @param:
        filename: a file containing a maze.
    """
    maze = Maze(open(filename, 'r').read())
    
    frontier = PriorityQueue()
    
    # a separate list to keep track of states we add to the frontier
    # as we cannot look inside elements of a queue.
    frontier_tracker = []
    
    explored = []
    
    curr_pos = maze.get_initial_state()
    frontier_tracker.append(curr_pos)
    
    frontier.put((multi_astar_cost(maze, curr_pos),
            curr_pos))
    
    while not frontier.empty():
        state = frontier.get()[1]
        explored.append(state)
        
        for neighbor in maze.moveable_nodes(state):
            if not has_visited(neighbor, explored) and not neighbor in frontier_tracker:
                if (neighbor.has_collected_all()):
                    display_solution(filename, "multi_astar", maze, neighbor, explored)
                    return
                frontier.put((multi_astar_cost(maze, neighbor),
                    neighbor))
                frontier_tracker.append(neighbor)
    print("Failed to collected all prizes.")    
    

def single_astar_cost(maze, state, prize_location):
    """
    The function to estimate the cost for the astar algorithm in the
    single-prize case.
    The heuristic function is the Manhattan distance from the current location
    to the prize.
    @param:
        maze: the maze.
        state: the current state.
        prize_location: the id of the prize in the maze.
    """
    cost_to_reach_node = state.cost
    estimate_cost_to_prize = maze.manhattan_distance(state.id, prize_location)
    
    return cost_to_reach_node + estimate_cost_to_prize
    
def multi_astar_cost(maze, state):
    """
    The function to estimate the cost for the astar algorithm in the
    single-prize case.
    The heuristic function in this case is the minimum Manhattan distance between
    two states from every possible pairs of prize nodes and the current location.
    
    @param:
        maze: the maze.
        state: the current state.
    """
    cost_to_reach_node = state.cost

    locations = list(state.prizes_locations)
    locations.append(state.id)
    
    min_distance = sys.maxsize
    
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = maze.manhattan_distance(locations[i], locations[j])
            if distance < min_distance: distance = min_distance
            
    estimate_cost_to_prize = min_distance * (len(locations) - 1)
    
    return cost_to_reach_node + estimate_cost_to_prize

def has_visited(state, explored):
    """
    Return True if a node has already been visited, False otherwise. A node is
    considered visited if there is a node with the same location and prizes found
    in the list of explored nodes.
    @param:
        algo_name: name of the algorithm used to generate the solution.
        maze: the maze.
        node: the node which contains the final state of the solution.
        explored: the list of nodes all the nodes expanded by the algorithm.
    """
    for visited_node in explored:
        if state == visited_node: return True
    
    return False

def display_solution(maze_name, algo_name, maze, state, explored):
    """
    Print the solution of maze along with the cost and the number of
    nodes expanded.
    @param:
        maze_name: name of the file containing a maze.
        algo_name: name of the algorithm used to generate the solution.
        maze: the maze.
        state: the state of the solution.
        explored: the list of nodes all the nodes expanded by the algorithm.
    """
    input = maze_name
    algo = algo_name
    path_cost = len(state.path)
    nodes_expanded = len(explored)
    
    with open("output.txt", "a") as output:
        output.write("\n\n\n---- Maze: %s ----\n" %(input))
        output.write("---- Algorithm: %s ----\n" %(algo))
        if algo == "multi_astar":
            print_maze_astar(output, maze, state)
        else:
            print_maze(output, maze, state)
        output.write("\nThe past cost of the solution is %s." %(path_cost))
        output.write("\nThe number of nodes expanded by the search algorithm is %s." %(len(explored)))
    output.close()
    
def print_maze(file, maze, state):
    """
    Print the solution of the maze.
    @param:
        file: name of the output file.
        maze: the maze.
        state: the state of the solution.
    """
    source = maze.get_source()
    
    for i in range(len(source)):
        if i not in state.path:
            file.write(source[i])
        else:
            file.write(maze.PATH)
    
    file.write("")

def print_maze_astar(file, maze, state):
    """
    Print the solution of the maze in the multi_astar case.
    @param:
        file: name of the output file.
        maze: the maze.
        state: the state of the solution.
    """
    prizes_locations = maze.get_initial_state().prizes_locations
    orders = {}
    index = 0
    
    for id in state.path:
        if id in prizes_locations and not id in orders:
            orders[id] = index
            index += 1
    
    for i in range(len(maze.source)):
        if i in orders:
            file.write(convert_prize_count(orders[i]))
        else:
            file.write(maze.source[i])
    
    file.write("")
    
def convert_prize_count(prize_count):
    """
    Convert the order that the prize that was found into a single-character format
    @param:
        prize_count: the order that the prize was found.
    """
    count = prize_count
    orders = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    return orders[prize_count]