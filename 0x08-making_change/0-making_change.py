#!/usr/bin/python3
"""
Module for makeChange function
"""

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations (integers).
        total (int): The target amount (integer).

    Returns:
        int: The fewest number of coins needed to reach the total, or -1 if the
             total cannot be met with the given coins.
    """
    if not isinstance(coins, list):
        raise TypeError("coins must be a list")
    if not all(isinstance(coin, int) and coin > 0 for coin in coins):
        raise ValueError("coins must be a list of positive integers")
    if not isinstance(total, int):
        raise TypeError("total must be an integer")
    if total < 0:
        raise ValueError("total must be a non-negative integer")

    if total <= 0:
        return 0

    # Initialize a list to track the minimum coins needed for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1