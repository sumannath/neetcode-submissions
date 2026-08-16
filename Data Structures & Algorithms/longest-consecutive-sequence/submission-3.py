class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hsh = set(nums)

        longest = 0
        for x in nums:
            if x-1 not in hsh:
                ln = 0
                while (x+ln) in hsh:
                    ln += 1
            
                longest = max(longest, ln)

        return longest