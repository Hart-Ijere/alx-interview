#!/usr/bin/python3
"""
This module contains the function `makeChange` that determines the fewest number
of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    :param coins: List of coin values (positive integers)
    :param total: Target total amount
    :return: Fewest number of coins needed to make total, or -1 if not possible
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    dp = [float("inf")] * (total + 1)  # Initialize DP array
    dp[0] = 0  # Base case

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(
                dp[amount], dp[amount - coin] + 1
            )

    return dp[total] if dp[total] != float("inf") else -1
