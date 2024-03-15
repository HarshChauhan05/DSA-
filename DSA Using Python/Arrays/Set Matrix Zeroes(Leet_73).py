class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)
        clmn = [False for _ in range(n)]
        rw = [False for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    clmn[j] = True
                    rw[i] = True

        for i in range(m):
            for j in range(n):
                if clmn[j] or rw[i]:
                    matrix[i][j] = 0
