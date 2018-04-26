# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java

# Test cases
# ==========

# Inputs:
#     (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# Output:
#     (int) 7

# Inputs:
#     (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# Output:
#     (int) 11

import Queue
from copy import deepcopy

class Maze:
    def __init__(self,m):
        self.maze=m
        self.n=len(m)
        self.m=len(m[0])

    def bounderies(self,i,j):
        # return all cardinal coordinates in scope of maze and not a wall
        return filter(

            lambda x: x[0]>-1 and x[0]<self.n and x[1]<self.m and x[1]>-1 and not self.maze[x[0]][x[1]]==1,
            
            [(i,j-1),(i-1,j),(i+1,j),(i,j+1)]
            
            )

    def traverse(self,direction=True):
        # used dijkastra algo for searching shortest path
        if direction:
            x,y=(0,0)
        else:
            x,y=(self.n-1,self.m-1)
        self.maze[x][y]=2
        q=Queue.Queue()
        q.put((x,y))
        while not q.empty():
            x,y=q.get()
            for (i,j) in self.bounderies(x,y):
                if self.maze[i][j]==0:
                    self.maze[i][j]=10000000000
                    q.put((i,j))
                else:
                    self.maze[x][y]=min(self.maze[x][y],self.maze[i][j]+1)

def answer(m):
    ans=10000000000
    maze=Maze(deepcopy(m))
    maze.traverse()
    # traverse both from starting and end point
    reversemaze=Maze(deepcopy(m))
    reversemaze.traverse(False)

    # if without removing wall, got best solution
    if maze.maze[-1][-1]==maze.n+maze.m-1:
        return maze.n+maze.m-1
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1:
                # wherever there is a wall, 
                # we check combinations of points around wall,
                # taking one point from forward traversal and one from backward
                boundriesfrommaze=filter(lambda x: not x==0,[maze.maze[x][y] for (x,y) in maze.bounderies(i,j)])
                boundriesfromreversemaze=filter(lambda x: not x==0,[reversemaze.maze[x][y] for (x,y) in reversemaze.bounderies(i,j)])
                for left in boundriesfrommaze:
                    for right in boundriesfromreversemaze:
                        ans=min(left+right,ans)
    # -1 because we started with 2, to avoid conflict with 1 of walls
    return ans-1

print answer(
    [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    )