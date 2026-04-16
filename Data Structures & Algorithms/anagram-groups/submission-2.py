import json

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_alpha = {}
        for str in strs:
            dict_str = self.getDict(str)
            if dict_str in dict_alpha:
                dict_alpha[dict_str].append(str)
            else:
                dict_alpha[dict_str] = [str]

        to_return = []
        for dict_items in dict_alpha:
            to_return.append(dict_alpha[dict_items])

        return to_return

    def getDict(self, str):
        dict_str  = {}

        for ch in str:
            if ch in dict_str:
                dict_str[ch] = dict_str[ch] + 1
            else:
                dict_str[ch] = 1

        return json.dumps(dict_str, sort_keys=True)