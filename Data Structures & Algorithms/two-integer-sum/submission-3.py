class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for idx, x in enumerate(nums):
            if x in nmap:
                nmap[x].append(idx)
            else:
                nmap[x] = [idx]

        print(nmap)

        for idx, x in enumerate(nums):
            to_find = target - x
            if to_find == x:
                if len(nmap[to_find]) > 1:
                    return [idx, nmap[to_find][1]]
            else:
                if to_find in nmap:
                    return [idx, nmap[to_find][0]]

        return None
