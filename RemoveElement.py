class Solution {
    public int removeElement(int[] nums, int val) {
        int index = 0;      //1  2
        for(int i = 0; i<nums.length; i++)
        {                       //i=0 -->3==3
                                //i=1 -->2!=3
                                //1=2 -->2!=3
                                //1=3 -->3==3
            if(nums[i]==val){
                //remove
            }
            else if(nums[i]!=val)
            {
                nums[index]=nums[i];
                 index++;                    // 0 index=2
                                            // 1 index=2
            }                         //2,3,2,3
                                      //2,2,3,3
        }
        return index;
    }
}