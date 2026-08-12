class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freq = {}
        for s in strs:
            fr = self.freq(s)
            if fr in char_freq:
               char_freq[fr].append(s)
            else:
                char_freq[fr] = [s]
        
        return list(char_freq.values())

    def freq(self, s: str) -> dict:
        freq = {}

        for x in s:
            if x in freq:
                freq[x] = freq[x] + 1
            else:
                freq[x] = 1

        return tuple(sorted(freq.items()))