class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.getDict(s)
        dict_t = self.getDict(t)
        
        if dict_s == dict_t:
            return True
        
        return False
        
            
    def getDict(self, s: str):
        dict_s = {}
        for ch in s:
            if dict_s.get(ch) is None:
                dict_s[ch] = 1
            else:
                dict_s[ch] = dict_s[ch] + 1
                
        return dict_s