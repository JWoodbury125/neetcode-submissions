class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            speed = (left + right)//2

            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + speed - 1)//speed

                if hours_needed > h:
                    break

            if hours_needed <= h:
                right = speed
            else:
                left = speed + 1

        return left