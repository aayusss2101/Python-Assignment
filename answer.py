'''
Checks whether the row and column number is valid 
Parameters:
    r (int): Row Number
    c (int): Column Number
    m (int): Total Number of Rows
    n (int): Total Number of Columns
Return:
    (bool): True if valid, False otherwise
'''
def isValid(r: int, c: int, m: int, n: int) -> bool:
    
    # Global visited variable
    global visited
    
    if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
        return False
    return True

'''
Applies DFS algorithm to visit all the elements reachable from border Os
Parameters:
    board (list[list[str]]): The board containing X and O
    r (int): Row Number
    c (int): Column Number
    m (int): Total Number of Rows
    n (int): Total Number of Columns
Returns:
    None
'''
def dfs(board: list[list[str]], r: int, c: int, m: int, n: int) -> None:
    
    # Returning if invalid row and column number
    if not isValid(r, c, m, n):
        return

    # Global visited variable
    global visited
    visited[r][c] = True
    
    # Returning if current element is X
    if board[r][c] == 'X':
        return
    
    # Modifying reachable Os to a temporary value
    board[r][c] = '$'

    # Traversing all the four board elements reachable from the current element
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(board, r+i, c+j, m, n)

'''
Flips all the surrounded Os
Parameters:
    board (list[list[str]]): The board containing X and O
Returns:
    None
'''
def solve(board: list[list[str]]) -> None:
    
    # Total number of rows
    m = len(board)
    # Total number of columns
    n = len(board[0])

    # Global visited variable
    global visited
    # Initialising visited variable
    visited = [[False]*n for i in range(m)]

    # Traversing elements on 1st and last row
    for j in range(n):
        dfs(board, 0, j, m, n)
        dfs(board, m-1, j, m, n)

    # Traversing elements on 1st and last column
    for i in range(m):
        dfs(board, i, 0, m, n)
        dfs(board, i, n-1, m, n)

    # Flipping O to X and temporary value to O 
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '$':
                board[i][j] = 'O'


if __name__ == "__main__":
    try:
        
        # Total Number of Rows
        m = int(input("Enter number of rows: "))
        # Total Number of Columns
        n = int(input("Enter number of columns: "))

        # Board
        board = [[]]*m

        print("Enter board: ")

        '''
        Taking board input
        For example, if you want board to be [['X','X'],['O','X']], give input in the form
        XX
        OX
        '''
        for i in range(m):
            board[i] = list(input())
        
        solve(board)
        
        # Final output board
        print(board)
        
    except:
        print("Some error occurred")
