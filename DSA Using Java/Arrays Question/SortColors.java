class Solution {
    public void sortColors(int[] nums) {
        int n=nums.length;
        int start =0, mid =0, end=n-1;
        while(mid<=end){
            if(nums[mid]==0){
                int temp=nums[start];
                nums[start]=nums[mid];
                nums[mid]=temp;
                start++;
                mid++;

            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                int temp=nums[mid];
                nums[mid]=nums[end];
                nums[end]=temp;
                end--;
            }
        }
    }
}