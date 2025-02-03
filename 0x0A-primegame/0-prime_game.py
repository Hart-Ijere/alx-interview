#!/usr/bin/python3

def sieve(n):
    """Returns a list where prime[i] is True if i is a prime number, otherwise False."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
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
    str: Name of the player with the most wins (Maria or Ben) or None if it's a tie.
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
    else:
        return None  # Tie
