#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins: A list of the values of the coins in your possession.
        total: The target amount to be met.

    Returns:
        The fewest number of coins needed to meet the total.
        0 if total is 0 or less.
        -1 if total cannot be met by any number of coins.
    """

    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)  # Initialize with infinity
    min_coins[0] = 0  # Base case: 0 coins needed for 0 amount

    for amount in range(1, total + 1):
        for coin in coins:
            if amount >= coin:
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
