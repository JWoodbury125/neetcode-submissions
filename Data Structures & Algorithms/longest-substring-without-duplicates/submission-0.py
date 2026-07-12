class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            
            len_curr_window = r - l + 1
            if len_curr_window > length:
                length = len_curr_window
        
        return length