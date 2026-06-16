class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] = freq[x] + 1
            else:
                freq[x] = 1

        buckets = [None] * 1001
        for key, val in freq.items():
            if buckets[val] is None:
                buckets[val] = [key]
            else:
                buckets[val].append(key)

        ctr = 1
        opt = []
        found = 0
        print(k)
        for x in range(1000, 0, -1):
            if buckets[x] is not None:
                nums = buckets[x]
                print(nums)
                for y in nums:                    
                    opt.append(y)
                    ctr = ctr + 1
                    print(ctr)
                    if ctr > k:
                        found = 1
                        break

                if found == 1:
                    break
        
        return opt
        