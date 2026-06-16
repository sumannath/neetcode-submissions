class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_strs = {}
        for s in strs:
            fq_s = self.get_freq_dist(s)
            if fq_s in all_strs:
                all_strs[fq_s].append(s)
            else:
                all_strs[fq_s] = [s]

        return list(all_strs.values())


    def get_freq_dist(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] = freq[idx] + 1

        return str(freq)