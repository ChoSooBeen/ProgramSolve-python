class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row-1
        flag = False
        while start <= end :
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][col-1] >= target :
                row = mid
                flag = True
                break
            
            if matrix[mid][0] >= target :
                end = mid - 1
            else :
                start = mid + 1
        
        if not flag :
            return False
        
        start = 0
        end = col-1
        while start <= end :
            mid = (start + end) // 2
            if matrix[row][mid] == target :
                return True
            if matrix[row][mid] > target :
                end = mid - 1
            else :
                start = mid + 1
        
        return False