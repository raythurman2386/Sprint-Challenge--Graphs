from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from utils import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited_graph = {}


# There is a potential function inside room.py
# I will explore that option once MVP is met
def check_neighbor_rooms(current_room, next_room):
    if current_room == next_room:
        return 'Same Room'
    elif current_room.n_to == next_room:
        return 'n'
    elif current_room.s_to == next_room:
        return 's'
    elif current_room.w_to == next_room:
        return 'w'
    elif current_room.e_to == next_room:
        return 'e'


# IF no adjacent room, BFS to find the shortest path to the
# next new room
def bfs(current_room, next_room):
    queue = Queue()
    queue.enqueue([current_room])
    visited = set()
    # while the queue is not empty
    while queue.size() > 0:
        # dequeue the first vertex
        path = queue.dequeue()
        current = path[-1]
    # if room is not visited
        if current not in visited:
            if current == next_room:
                return path
        # mark as visited
            visited.add(current)
        # enqueu all neighboring rooms
            for neighbor in current.get_exits():
                new_path = list(path)
                new_path.append(current.get_room_in_direction(neighbor))
                queue.enqueue(new_path)


# DFS
# Stack to keep track of room
# add the player's current room to the stack
# Track visited rooms with a set
# while stack size > 0
# pop off the stack for the path
# get the current from the path array path[-1]
# check the adjacent rooms from the players position
#
# if the current room is not in visited
# add to visited
#
# check neighbors after each node removed from stack
#
# else, if not adjacent, BFS to shortest path to new room
# once room is found, figure out the directions
# keep track of the directions
# check the neighbor of each room in shortest path


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
