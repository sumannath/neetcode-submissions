class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}
        for s in strs:
            key = self.get_hash_key(s)
            if key in grps:
                grps[key].append(s)
            else:
                grps[key] = [s]

        #print(grps)
        return list(grps.values())

    def get_hash_key(self, s):
        hash_key = [0] * 26
        for ch in s:
            num_idx = ord(ch) - ord('a')
            hash_key[num_idx] = hash_key[num_idx] + 1

        return "".join([f"{chr(idx + ord('a'))}{val}" for idx, val in enumerate(hash_key)])
        