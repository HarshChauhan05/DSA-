class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target>matrix[-1][-1]:
            return False
        cl=len(matrix[0])
        rw=len(matrix)
        low=0
        high=cl*rw-1
        while(low<=high):
            mid = (low + high) // 2
            if target==matrix[int(mid/cl)][mid%cl]:
                return True
            elif target<matrix[int(mid/cl)][mid%cl]:
                high=mid-1
            else:
                low=mid+1
        return False
