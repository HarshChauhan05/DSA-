class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                break
        else:
            nums.reverse()
            return
        for j in range(n-1,-1,-1):
            if nums[j]>nums[i]:
                break
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]= reversed(nums[i+1:])
              
