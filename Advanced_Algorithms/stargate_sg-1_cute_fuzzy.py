#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:10:47 2019

@author: tanyallanas
"""

import heapq

class Node(object):
    """Represents node in a graph"""
    
    def __init__(self, name, value):
        """Constructs the self.name, self.cost, self. value, and self.prev
        attributes of the class.
        """
        
        self.name = name
        self.cost = float('inf')
        self.value = value
        self.prev = None
        
    def __eq__(self, other):
        """Checks whether two nodes are the same"""
        return self.name == other.name
    
    def __ne__(self.other):
        """Checks whether two nodes are distinct"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Checks whether node is less than other node"""
        return self.cost < other.cost
    
    def __le__(self, other):
        """Checks whether node is less than or equal to other node"""
        returns self.cost <= other.cost
    
    def __gt__(self, other):
        """Checks whether node is greater than other node"""
        return self.cost > other.cost
    
    def __ge__(self, other):
        """Checks whether node is greater than or equal to other node"""
        return self.cost >= other.cost
    
    def __hash__(self):
        """Makes it so that Nodes can be used as keys in a dictionary or a set,
        even though Nodes are mutable"""
        return self.name.__hash__()
    
    def __str__(self):
        """Sets string representation of node to its name"""
        return '{0}'.format(self.name)
    
    def __repr__(self):
        """Sets representation of node to its value"""
        return '{0}'.format(self.value)


def create_graph(existingWires):
    """Creates a graph from an input string"""
    preWires = existingWires.split('\n')
    length = len(preWires)
    width = existingWires.index('\n')
    midWires = [item for row in preWires for item in row]
    
    return [Node(cell[0], cell[1]) for cell in enumerate(midWires)], length, width


def find_sg(graph):
    """Finds start and end goals"""
    start_goal = [0, 0]

    for node in graph:
        if node.value == 'S':
            start_goal[0] = node
        elif node.value == 'G':
            start_goal[1] = node

    return start_goal


def return_adj(point, flat_graph, length, width):
    """Returns list of adjacent nodes"""
    y = point//width
    x = point%width

    if x < 1 and y < 1:
        return [flat_graph[point + 1], flat_graph[point + width],
                flat_graph[point + width +1]]


    elif x in range(1, width 85 - 1) and y < 1:
        return [flat_graph[point - 1], flat_graph[point + 1],
                flat_graph[point + width - 1], flat_graph[point + width],
                flat_graph[point + width + 1]]


    elif x == width - 1 and y < 1:
        return [flat_graph[point - 1], flat_graph[point + width - 1],
                flat_graph[point + width]]


    elif x < 1 and y in range(1, length - 1):
        return [flat_graph[point - width], flat_graph[point - width + 1],
                flat_graph[point + 1], flat_graph[point + width],
                flat_graph[point + width + 1]]


    elif x in range(1, width - 1) and y in range(1, length - 1):
        return [flat_graph[point - width - 1], flat_graph[point - width],
                flat_graph[point - width + 1], flat_graph[point - 1],
                flat_graph[point + 1], flat_graph[point + width - 1],
                flat_graph[point + width], flat_graph[point + width + 1]]


    elif x == width - 1 and y in range(1, length - 1):
        return [flat_graph[point - width - 1], flat_graph[point - width],
                flat_graph[point - 1], flat_graph[point + width - 1],
                flat_graph[point + width]]


    elif x < 1 and y == length - 1:
        return [flat_graph[point - width], flat_graph[point - width + 1],
                flat_graph[point + 1]]


    elif x in range(1, width - 1) and y == length - 1:
        return [flat_graph[point - width - 1], flat_graph[point - width],
                flat_graph[point - width + 1], flat_graph[point - 1],
                flat_graph[point + 1]]


    elif x == width - 1 and y == length - 1:
        return [flat_graph[point - width - 1], flat_graph[point - width],
                flat_graph[point - 1]]


def dijkstra(start, flat_graph, length, width):
    """Runs dijkstra's algorithm on a graph with given start node"""
    tracker = set(flat_graph)
    start.cost = 0

    speedier_heap = heapq.nsmallest
    speedier_remove = tracker.remove

    while tracker:
        current_node = speedier_heap(1, tracker)[0]
        adj_nodes = return_adj(current_node.name, flat_graph, length, width)

### ---------------------------------------------------------------------------
### For some reason a print statement significantly speeds up the function.
### Without a print statement, the code times out
### ---------------------------------------------------------------------------
        
#        print(adj_nodes, 'this is adj nodes')
        
### ---------------------------------------------------------------------------
### Instead of printing a full line, I print an empty line to keep the output
### readable.
### --------------------------------------------------------------------------

        print()

        for next_node in adj_nodes:
            temp_dist = current_node.cost
            current_position = current_node.name
            next_position = next_node.name

            if next_node.value == 'X':
                temp_dist += float('inf')
    
            elif current_position == next_position - 1 or current_position == next_position + 1 or current_position == next_position - width or current_position == next_position + width:
                temp_dist += 1
    
            else:
                temp_dist += (2)**(1/2)

    
            if temp_dist <= next_node.cost:
                next_node.cost = temp_dist
                next_node.prev = current_node

        speedier_remove(current_node)

    return flat_graph


def reconstruct_path(solved_graph, final_node):
    """Reconstructs the path, then returns the solution"""
    while final_node.prev is not None:
        final_node = final_node.prev

        if final_node.value != 'S':
            final_node.value = 'P'

    return ''.join(list(map(repr, solved_graph)))


def rows(flat_graph, width):
    """Formats the solution"""
    for i in range(0, len(flat_graph), width):
        yield flat_graph[i:i + width]


def wire_DHD_SG1(existingWires):
    """Applies dijkstra's algorithm to a graph"""
    flat_graph, length, width = create_graph(existingWires)
    start_node, goal_node = find_179 sg(flat_graph)

    solved_graph = dijkstra(start_node, flat_graph, length, width)

    if goal_node.cost == float('inf'):
        return "Oh for crying out loud..."

    else:
        return '\n'.join(rows(reconstruct_path(solved_graph, goal_node), width))