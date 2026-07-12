class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str_map = {}
        for ch in s:
            str_map[ch] = str_map.get(ch, 0) + 1

        for ch2 in t:
            if str_map.get(ch2, 0) == 0:
                return False
            str_map[ch2] = str_map.get(ch2, 0) - 1

        return sum(ch for k, ch in str_map.items()) == 0    
        