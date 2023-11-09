prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
# prices = [2,4,1]

# can buy/sell stock
# can holt one stock a day 
# can buy and sell immediately on the same day

def profit(prices): # better for time
    n = len(prices)

    buy = prices[0]
    profit = 0

    if n > 1:
        for i in range(n):

            if prices[i] < prices[i+1] and prices[i] < buy: 
                buy = prices[i]

            print(f"{prices[i]} > {prices[i+1]} and {buy} < {prices[i+1]}")

            if prices[i] > prices[i+1] and buy < prices[i]:
                profit += (prices[i]-buy)
                buy = prices[i+1]

            if i+1 == n-1: 
                if prices[i+1] > buy: 
                    profit += (prices[i+1]-buy)
                    break
                break

    return profit

def profit2(prices): #better for memory
    n = len(prices)

    profit = 0

    if n > 1:
        for i in range(1, n):

            if prices[i] > prices[i-1]: 
                profit += prices[i] - prices[i-1]

    return profit

   

