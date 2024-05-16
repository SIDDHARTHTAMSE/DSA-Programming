class Solution {
    public int removeDuplicates(int[] nums) {
      int j=1;
      for(int i=1; i<nums.length; i++) //i=1, i=2
      {
        if(nums[i-1]==nums[i]) //1-1=0--> 1==1
                              
        {

        }
        else if(nums[i-1]!=nums[i]) // 2-1=1--> 1==2 
        {
            nums[j]=nums[i];
            j++;
        }
      }
      return j;
    }
}