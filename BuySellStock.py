def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    i = 1
    while i < len(prices):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i]-prices[i-1]
        i += 1
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,1,2,5,4,28]))
        