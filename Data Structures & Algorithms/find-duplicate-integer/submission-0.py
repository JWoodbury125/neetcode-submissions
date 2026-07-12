class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        nums = Counter(nums)

        for k, v in nums.items():
            if v > 1:
                return k

        return
        