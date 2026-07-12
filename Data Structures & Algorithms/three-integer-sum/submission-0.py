class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]: continue
            l = n + 1
            r = len(nums) - 1
            while l < r:
                if nums[n] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[n] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[n], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1

        return res