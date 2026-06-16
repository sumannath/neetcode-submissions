class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = self.freqMatrix(s)
        freq_t = self.freqMatrix(t)
        return freq_s == freq_t
    
    def freqMatrix(self, s: str) -> dict:
        freq_dict = {}
        for x in s:
            if x in freq_dict:
                freq_dict[x] = freq_dict[x] + 1
            else:
                freq_dict[x] = 1

        return freq_dict