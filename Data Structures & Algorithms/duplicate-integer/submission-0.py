class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for x in nums:
            if x in elements:
                return True
            else:
                elements[x] = 1
        
        return False
        