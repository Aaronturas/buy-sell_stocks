def buy_sell_stocks(prices):
    # Write your code here
    maxPro = -1
    minNum = prices[0]#set minNum to first element of prices in order to compare to find lowest
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):#second loop needs to start after i in order to compare i and j
            if j > i:#if next element is greater than i then we find the difference
                minNum = min(minNum, prices[i])
        maxPro = max(maxPro, prices[i] - minNum)
    if maxPro != 0:
        return maxPro
    else:#if cannot find any profit return 0
        return 0

#TestCases
prices = [7,1,5,3,6,4]
print('Max Profit of', prices, 'is :', buy_sell_stocks(prices), '\n')

prices = [7,6,4,3,1]
print('Max Profit of', prices, 'is :', buy_sell_stocks(prices),'\n')