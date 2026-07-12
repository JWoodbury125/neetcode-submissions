class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(x, path):
            if x == len(nums):
                res.append(path[:])
                return
            if nums[x] not in path:
                path.append(nums[x])
                backtrack(x+1, path)
                path.pop()

            backtrack(x+1, path)
        
        backtrack(0, [])
        return res