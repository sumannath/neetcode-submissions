class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            x = nums[i]
            left = target - x

            try:
                left_idx = nums.index(left, i+1)
                return [i, left_idx]
            except ValueError:
                pass
        return []