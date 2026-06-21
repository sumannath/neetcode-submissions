class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_d = set(nums)
        longest = 0
        for x in nums:
            if x-1 in seq_d:
                pass
            else:
                current_num = x
                current_streak = 1

                while (current_num+1) in seq_d:
                    current_num = current_num + 1
                    current_streak = current_streak + 1

                longest = max(longest, current_streak)

        return longest