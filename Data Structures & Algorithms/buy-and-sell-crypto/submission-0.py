class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left, right = 0, 1

        while(left < len(prices) and right < len(prices) ):
            print('at line 8 -> ', left, right)
            if prices[left]<prices[right]:
                while right < len(prices) and prices[right] > prices[left]:
                    print('at line 11 -> ', left, right)
                    max_profit = max(max_profit, prices[right]-prices[left])
                    right = right+1

            elif prices[left] >= prices[right]:  
                while right<len(prices) and prices[left] >= prices[right]:
                    print('at line 17 -> ', left, right)
                    left+=1
                    right+=1

            

        return max_profit