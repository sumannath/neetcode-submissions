class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for index, value in enumerate(nums):
            if value in hashmap:
                return True
            hashmap[value] = 0

        return False
        