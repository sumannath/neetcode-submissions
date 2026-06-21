import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(ch for ch in s if ch.isalnum()).lower()

        print(cleaned_s)
        
        x = 0 
        y = len(cleaned_s) - 1

        is_palin = True
        while x < y:
            if cleaned_s[x] != cleaned_s[y]:
                is_palin = False
                break
            x = x + 1
            y = y - 1

        return is_palin