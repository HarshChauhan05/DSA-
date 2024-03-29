class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        flag=[0 for _ in range(len(nums)-1)]
        for i in nums:
            flag[i-1]+=1
        for i in range(len(flag)):
            if flag[i]>1:
                return i+1