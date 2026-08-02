class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # the OG binary search is while low <= high, so this one must use a similar termination

        m = len(matrix) # rows 
        n = len(matrix[0]) # cols

        # go into the middle row first col, if that is > target, go to lesser row, else go through that row
        # if it is not in that row, move onto the next rows first col, if that is > target it is not in the matrix
        low = 0
        high = m * n
        
        while low <= high:

            mid = (low + high) // 2
            
            i = (mid-1) // n
            j = (mid-1) % n 
            print(i,j)
            
            if mid == 0:
                i = mid // n
                j = mid % n
            

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False