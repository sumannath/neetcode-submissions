class Solution {
    public boolean hasDuplicate(int[] nums) {
        int length = nums.length;

        if(length == 1) return false;

        Arrays.sort(nums);
        for(int i = 1 ; i < nums.length ; i++) {
            int lastNum = nums[i - 1];
            if(lastNum == nums[i]) {
                return true;
            }
        }

        return false;
    }
}
