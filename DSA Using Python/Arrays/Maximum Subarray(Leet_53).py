class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=nums[0]
        max_ending_here=0
        for i in nums:
            max_ending_here=max_ending_here+i
            if max_so_far<max_ending_here:
                max_so_far=max_ending_here
            if max_ending_here<0:
                max_ending_here=0
        return max_so_far
