class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlength = 0
        counts = collections.defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            maxlength = max(maxlength, r - l + 1)
        return maxlength