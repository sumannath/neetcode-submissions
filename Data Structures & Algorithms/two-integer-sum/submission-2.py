class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc_mtx = {}
        for idx, item in enumerate(nums):
            if item in loc_mtx:
                loc_mtx[item].append(idx)
            else:
                loc_mtx[item] = [idx]

        #print(loc_mtx)

        for x in loc_mtx:
            to_find = target - x
            if to_find == x:
                if len(loc_mtx[to_find]) == 1:
                    continue
            if to_find in loc_mtx:
                if len(loc_mtx[to_find]) == 1:
                    return [loc_mtx[x][0], loc_mtx[to_find][0]]
                else:
                    return [loc_mtx[x][0], loc_mtx[x][1]]
