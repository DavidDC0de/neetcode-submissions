class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                new_diff = prices[r] - prices[l]
                max_diff = max(max_diff, new_diff)

            else:
                l = r

            r+=1
        return max_diff