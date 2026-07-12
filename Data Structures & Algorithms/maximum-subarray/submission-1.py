class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        left = 0
        maxL, maxR = 0, 0
        curSum = 0

        for right in range(len(nums)):
            if curSum < 0:
                curSum = 0
                left = right

            curSum += nums[right]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = left, right

        return sum(x for x in nums[maxL:maxR+1])