class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        for i in range(len(matrix)):
                if matrix[i][0] <= target<=matrix[i][-1]:
                    l, r = 0, len(matrix[i])-1
                    while l <=r:
                        m = l + (r - l) // 2
                        if target > matrix[i][m]:
                            l = m+1
                        elif target < matrix[i][m]:
                            r = m -1
                        else: 
                            return True    
            
        return False
        