class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # -> x(o) len(board[0]) 
        # ^ y(o) len(board)
        # |

        for i in range(0,9):
            x_set = set()
            for j in range(0, 9):
                value = board[i][j]
                if value == ".":
                    continue
                if  value in  x_set:
                    return False
                x_set.add(value)    


        for i in range(0,9):
            y_set = set()
            for j in range(0, 9):
                value = board[j][i]
                if value == ".":
                    continue
                if  value in  y_set:
                    return False
                y_set.add(value)  

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                xy_set = set()
                for k in range(i,i+3):
                    for l in range(j, j+3):
                        value = board[k][l]
                        if value == ".":
                          continue
                        if  value in  xy_set:
                          return False
                        xy_set.add(value)  


        return True         
                    

