class Solution:
    def fact(self,i,j):
        return factorial(i)//(factorial(i-j)*factorial(j))
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            ans=[]
            for j in range(i+1):
                ans.append(self.fact(i,j))
            res.append(ans)
        return res
