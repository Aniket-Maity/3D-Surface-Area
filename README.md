# This is a hackerrank medium level problem
--------------------------------------------
# problem statement
-----------------------

The hint has been read from the discussion list. If the 3d surface made of same-sided cubes then it becomes easy to calculate 3d surface. We have to look at the 3D surface from the top view, that way we can have a 2D surface with height values of each cell.

From here we have to check the neighbors of the each cell. For example, the cell on top-left has no neighbors on the left and top side, so we can accumulate side surfaces. On the right and bottom, it has neighbors but both of them are smaller than 4. That is why we can accumulate those sides too. Finally, top and bottom surfaces areas are always going to be same H x W, that is why the area can be initialized with sumArea = (H x W x 2)
* input
* 3 3
* 1 3 4
* 2 2 3
* 1 2 4
* output
* 60

### test case 1 is attached in TestCase1.txt file
* output:
299152