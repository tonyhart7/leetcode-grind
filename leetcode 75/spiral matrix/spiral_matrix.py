class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # iterate top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # iterate right colum
            for i in range(top, bottom):
                res.append(matrix[i][right -1])
            right -= 1 #shift right pointer to left
            
            if not (left < right and top < bottom):
                break # break loop if we done with top row and right column
            
            #iterate bottom in reverse order
            for i in range( right -1, left -1, -1):
                res.append(matrix[bottom -1][i])
            bottom -=1
            
            #iterate the rest 
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res