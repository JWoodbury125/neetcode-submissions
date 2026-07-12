class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}

        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in num_map:
                if num_map[diff] < idx:
                    return [num_map[diff] + 1, idx + 1]
        
            num_map[num] = idx

        return []