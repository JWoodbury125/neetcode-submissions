class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], idx]
            prev[num] = idx
        return
        