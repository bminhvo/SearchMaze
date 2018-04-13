# Vuong Khuat & Minh Vo
# CS365 - AI & Machine Learning
# Lab A
# vdkhuat16_mbvo14_maze.py

import math

class State:
    """
    A State class with four data members: id, cost, path, prizes_locations.
    id is an index of the maze string, which can be used to get the current location
    in the maze.
    """
    def __init__(self, id, cost, path, prizes_locations):
        """Create a new state instance.
        
        id                 the id of the current location in the maze
        cost               the path cost to get from the initial location to the current one  
        path               the path to get from the initial location to the current one
        prizes_locations   the locations of all the prizes in the maze
        """
        self.id = id
        self.cost = cost
        self.path = path
        self.prizes_locations = prizes_locations
        
    def has_collected_all(self):
        """This is our goal test. Return True if we have collected all
        the prizes, False otherwise.
        """
        return len(self.prizes_locations) == 0
        
    def __eq__(self, state2):
        return (self.id == state2.id) and (self.prizes_locations == state2.prizes_locations)
        
    # The two ordering functions below only serve to order states in a priority 
    # queue when their priorities are equal.
    def __gt__(self, state2):
        return self.id > state2.id
        
    def __lt__(self, state2):
        return self.id < state2.id

class Maze:
    """
    This is the representation of a maze object. Each maze object holds the source
    string of the maze and the initial state of the world.
    """

    STEP_COST = 1
    WALL = '%'
    START = 'P'
    PRIZE = '.'
    PATH = '#'
    
    WEST = "WEST"
    EAST = "EAST"
    SOUTH = "SOUTH"
    NORTH = "NORTH"
    DIRECTIONS = [WEST, EAST, SOUTH, NORTH]
    
    def __init__(self, source):
        self.source = source
        self.width = source.find("\n") + 1
                
        starting_index = source.find(self.START)
        self.initial_state = State(starting_index, 0, [], self.get_prizes_locations())
            
    def get_source(self):
        """
        Return the source string of the maze.
        """
        return self.source
    
    def get_prizes_locations(self):
        """
        Return the locations (indices) of all the prizes in the maze.
        """
        locations = set()
        
        for i in range(len(self.source)):
            if self.source[i] == self.PRIZE:
                locations.add(i)
                
        return locations
        
    def get_initial_state(self):
        """
        Returns the state which contains the initial state of the world.
        """
        return self.initial_state
        
    def move(self, state, dir):
        """
        Move the agent one unit in the specified direction. Also return the new state
        resulting from the move, but return None if the move is not possible 
        (i.e. moving into a wall).
        @param:
            state: The current state.
            dir: The direction to move to.
        """
        new_id = -1
        if dir == self.WEST:
            new_id = state.id - 1
        if dir == self.EAST:
            new_id = state.id + 1
        if dir == self.NORTH:
            new_id = state.id - self.width
        if dir == self.SOUTH:
            new_id = state.id + self.width   
        
        if not self.source[new_id] == self.WALL:
            new_path = list(state.path)
            new_path.append(new_id)
            
            new_prizes_locations = set(state.prizes_locations)
            if new_id in new_prizes_locations:
                new_prizes_locations.remove(new_id)
            
            new_state = State(new_id,
                            state.cost + self.STEP_COST,
                            new_path,
                            new_prizes_locations)
            
            return new_state
            
        return None
      
    
    def move_west(self, state):
        """
        Return the new state when the agent moves to the West.
        """
        return self.move(state, self.WEST)
        
    def move_east(self, state):
        """
        Return the new state when the agent moves to the East.
        """
        return self.move(state, self.EAST)
        
    def move_north(self, state):
        """
        Return the new state when the agent moves to the North.
        """
        return self.move(state, self.NORTH)
        
    def move_south(self, state):
        """
        Return the new state when the agent moves to the South.
        """
        return self.move(state, self.SOUTH)
            
    def moveable_nodes(self, state):
        """
        Return a list of new states that that result from the agent moving,
        if such moves are possible.
        """
        temp = [self.move(state, dir) for dir in self.DIRECTIONS]
        return [state for state in temp if state is not None]
    
    def get_coords(self, state_id):
        """
        Take the id (which is the index of a character in the maze string)
        and convert it to a tuple representing the Cartisian coordiates.
        """
        x = state_id // self.width
        y = state_id % self.width
        return (x, y)
        
    def manhattan_distance(self, state1_id, state2_id):
        """
        Return the Manhattan distance between the two specified locations.
        """
        x1, y1 = self.get_coords(state1_id)
        x2, y2 = self.get_coords(state2_id)
        return int(math.fabs(x1 - x2) + math.fabs(y1 - y2))
    
    