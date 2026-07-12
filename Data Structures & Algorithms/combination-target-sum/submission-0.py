class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(x, path):
            current_sum = sum(path)
            if current_sum == target:
                res.append(path[:])
                return
            
            if x == len(nums) or current_sum > target:
                return

            path.append(nums[x])
            backtrack(x, path)
            path.pop()
            backtrack(x+1, path)
        
        backtrack(0, [])
        return res