#!/usr/bin/python3
"""
Prime Game Module

Maria and Ben are playing a game using a set of consecutive integers
from 1 to n. They take turns choosing a prime number and removing it
along with its multiples. Maria always goes first, and the player who
cannot make a move loses.

This module provides a function `isWinner` to determine the overall
winner after x rounds.

Functions:
    - sieve(n): Returns a list indicating prime numbers up to n.
    - count_primes(n, primes): Counts prime numbers up to n.
    - isWinner(x, nums): Determines the winner based on optimal gameplay.

Usage:
    - Call `isWinner(x, nums)` with the number of rounds `x` and a list
      of `n` values.
    - The function returns the name of the player who wins the most rounds.
"""


def sieve(n):
    """
    Returns a list where prime[i] is True if i is a prime number,
    otherwise False.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def count_primes(n, primes):
    """Returns the number of prime numbers up to n."""
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """
    Determines the winner of the game.

    Parameters:
    x (int): Number of rounds
    nums (list): List containing values of n for each round

    Returns:
    str: Name of the player with the most wins ("Maria" or "Ben"),
         or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)  # Get the largest n in all rounds
    primes = sieve(max_n)  # Precompute prime numbers up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)

        # If Maria has an odd number of moves, she wins, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None  # Tie
