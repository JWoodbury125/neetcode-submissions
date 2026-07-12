class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSum = float('inf')
        l = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minSum = min(minSum, r - l + 1)
                currSum -= nums[l]
                l += 1
        return minSum if minSum != float('inf') else 0