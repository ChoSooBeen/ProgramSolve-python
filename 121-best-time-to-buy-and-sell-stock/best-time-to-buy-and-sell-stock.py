class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        pre = 0

        if prices :
            pre = prices.pop()
        while prices :
            t = prices.pop()
            if t > pre :
                pre = t
            else :
                result = max(result, pre - t)
        return result