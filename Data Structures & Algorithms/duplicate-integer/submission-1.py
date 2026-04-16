class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if dict_num.get(num) is None:
                dict_num[num] = 1
            else:
                dict_num[num] = num + 1
                return True
        
        return False