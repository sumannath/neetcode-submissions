class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.char_freq(s) == self.char_freq(t)
    
    def char_freq(self, s: str) -> dict:
        freq = {}
        for x in s:
            if x in freq:
                freq[x] = freq[x] + 1    
            else:
                freq[x] = 1

        return freq




        