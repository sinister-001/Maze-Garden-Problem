# Maze-Garden-Problem

Given a garden in form of a 7 x 7 Maze with empty blocks, flowers and obstacles filled in it. Find the *shortest path* in which you will be starting from (0,0) and reach (6,6) along with that you have to **maximize** the *number of flowers collected* in the way. Note that you can not *move diagonally* in the given maze. Modify the **A* - Algorithm** according to this problem by considering the **heuristic function** to be taken as *maximizing the numbers of flowers collected*.

The following inputs will be present in each cell of the maze:
  * 0 - represents an epty block to which you can move
  * 1 - represents an obstacle which you cannot break or pass-through
  * 2 - represents the flowers that you have to collect

### Sample Input
0 0 0 0 0 0 0<br>
0 1 0 2 0 0 1<br>
0 2 0 1 0 2 0<br>
0 1 0 1 0 2 0<br>
0 0 0 0 0 0 0<br>
0 0 1 0 2 0 2<br>
0 0 0 0 0 0 0<br>

<b>Find the shortest path in this problem, path length and try to display the way in the matrix form <i>(like denoting the coordinates in form of any special character like *, >, etc.)<i> as the part of output?<b>
