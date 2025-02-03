#!/usr/bin/python3
"""
Module for isWinner function.
"""

def isWinner(x, nums):
    """
    Determines the winner of a game based on prime number selection.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n values, where each n represents the upper
                     limit of the set of consecutive integers for a round.

    Returns:
        str or None: The name of the player who won the most rounds
                     ("Maria" or "Ben"), or None if the winner cannot be
                     determined.
    """

    def count_primes(n):
        """Counts the number of primes up to n using the Sieve of Eratosthenes."""
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i*i, n + 1, i):
                    is_prime[multiple] = False
        return sum(is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = count_primes(n)
        if primes % 2 == 0:  # Even number of primes, Ben wins
            ben_wins += 1
        else:  # Odd number of primes, Maria wins
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print(isWinner(3, [5, 1, 7]))  # Example usage
    print(isWinner(5, [1, 1, 1, 1, 1])) # Example usage