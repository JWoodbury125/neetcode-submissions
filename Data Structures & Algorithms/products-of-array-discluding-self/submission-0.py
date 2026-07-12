import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for idx in range(len(nums)):
            if idx == 0:
                result.append(math.prod(x for x in nums[1:]))
            elif idx == len(nums) - 1:
                result.append(math.prod(x for x in nums[:len(nums) - 1]))
            else:
                result.append(math.prod(x for x in nums[:idx]) * math.prod(y for y in nums[idx +1:]))

        return result    