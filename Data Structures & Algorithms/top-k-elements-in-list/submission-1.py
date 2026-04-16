class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] = freq[x] + 1
            else:
                freq[x] = 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_freq.keys())[0:k]