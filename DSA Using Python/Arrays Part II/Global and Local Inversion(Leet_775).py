class Solution(object):
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        cnt=0
        while left<=mid and right<=high:
            if arr[left]<arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                cnt+=(mid-left+1)
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1

        while right<=high:
            temp.append(arr[right])
            right+=1

        return cnt
        
    def mergesort(self,nums,low,high):
        cnt=0
        if low>=high:
            return False
        mid=(low+high)//2
        cnt+=self.mergesort(nums,low,mid)
        cnt+=self.mergesort(nums,mid+1,high)
        cnt+=self.merge(nums,low,mid,high)
        return cnt

        
    def li(self,nums,n):
        cnt=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                cnt+=1
        return cnt
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        return True if self.li(nums,n)==self.mergesort(nums,0,n-1) else False
        
