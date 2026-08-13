class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for x in nums:
            if x in freq_map:
                freq_map[x] = freq_map[x] + 1
            else:
                freq_map[x] = 1

        # print(freq_map)
        N = 1000
        buckets = [ [] for _ in range(N) ]
        # print(buckets)
        for key, val in freq_map.items():
            buckets[val-1].append(key)

        z = 0
        opt = []
        for x in range(999, -1, -1):
            if len(buckets[x]) != 0 and z < k:
                for element in buckets[x]:
                    opt.append(element)
                z += len(buckets[x])

        return opt
         