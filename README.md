# Algorithm

I have used a DFS based approach to solve the problem. As mentioned in the question, we are only required to flip those Os which are surrounded on all four sides by X. In a grid of only X and O, there is only one way this could be possible, if the O element touches the boundary directly or indirectly on any of the four sides. I have expanded my algorithm on this idea. For every O element on the boundaries of grid, I have applied DFS with that element as root in order to find all the connected Os to this element. To differentiate this O from the O which is surrounded on all four sides, I have replaced these Os with a temporary character, \$, during the DFS procedure. Hence, after the DFS will be completed, we will be only left with three characters on the board, namely, X, O and \$. Finally, I have replaced all the Os with X and reverted all the \$s to O.

Steps Taken to Solve:
1. Traverse the board's boundary elements and search for O's
2. Perform DFS from the position of every O we locate.
3. Convert all O characters in DFS to a temporary character \$.
4. Flip remaining O to X and replace \$ with O
