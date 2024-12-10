#!/usr/bin/python3
def isWinner(x, nums):
    """Determine the winner of a prime game."""
    if x < 1 or not nums:
        return None

    # Find the maximum value of n to generate primes
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each game
    for n in nums:
        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
