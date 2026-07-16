class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(x, path):
            if x == len(nums):
                res.append(path[:])
                return
            
            # All subsets that include nums[x]
            path.append(nums[x])
            backtrack(x+1, path)
            path.pop()

            # All subsets that don't include nums[x] and its duplicates
            while x + 1 < len(nums) and nums[x] == nums[x+1]:
                x += 1

            backtrack(x+1, path)

        backtrack(0, [])

        return res
            