class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[i],nums1[i+n]=nums1[i+n],nums1[i]
        j=m
        k=0
        print(nums1)
        for i in range(n+m):
            if j<m+n and k<n and (nums1[j]<nums2[k]):
                nums1[i]=nums1[j]
                j+=1
            elif k<n:
                nums1[i]=nums2[k]
                k+=1
