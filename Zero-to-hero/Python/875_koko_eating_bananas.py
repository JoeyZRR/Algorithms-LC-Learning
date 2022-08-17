class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) ==  h:
            return max(piles)
        def curTime(k, piles):
            cur = 0
            for pile in piles:
                if pile <= k:
                    cur += 1
                else:
                    cur += math.ceil(pile/k)
            return cur
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            time = curTime(mid, piles)
            if time > h:
                left = mid + 1
            else:
                right = mid
        return left