class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        left, right = 0, len(matrix) -1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                row = mid
                lo, high = 0, len(matrix[row])-1
                while lo <= high:
                    m = (lo + high) // 2
                    if matrix[row][m] > target:
                        high = m - 1
                    elif matrix[row][m] < target:
                        lo = m + 1
                    else:
                        return True
                return False
        return False

        