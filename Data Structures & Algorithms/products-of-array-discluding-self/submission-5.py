class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prd = [1] * len(nums)
        suf_prd = [1] * len(nums)

        prd = 1
        for idx, x in enumerate(nums):
            pre_prd[idx] = prd
            prd = prd * x
            
        prd = 1
        for x in range(len(nums) - 1, -1, -1):
            print(x)
            suf_prd[x] = prd
            prd = prd * nums[x]
        
        return [pre_prd[i] * suf_prd[i] for i in range(0, len(nums))]