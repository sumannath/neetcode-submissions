class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        for index, ch in enumerate(s):
            if ch in hashmapS:
                hashmapS[ch] += 1 
            else:
                hashmapS[ch] = 1

        for index, ch in enumerate(t):
            if ch in hashmapT:
                hashmapT[ch] += 1 
            else:
                hashmapT[ch] = 1

        return hashmapS == hashmapT