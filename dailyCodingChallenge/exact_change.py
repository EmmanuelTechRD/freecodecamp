# freeCodeCamp challenge: Given an integer amount in cents, 
# return the number of distinct ways to make exact change using 
# pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).
def exact_change(amount: int) -> int:
    coins = [1, 5, 10, 25]

    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]