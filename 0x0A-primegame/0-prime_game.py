#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers denoting the upper
        limits of each round.

    Returns:
        str: The name of the player who won the most
        rounds (either "Ben" or "Maria").
        None: If the winner cannot be determined.
    """
    # Check for invalid input
    if x <= 0 or nums is None or x != len(nums):
        return None

    # Initialize scores
    ben = 0
    maria = 0

    # Generate a list of prime numbers up to the
    # maximum number in nums using the Sieve of Eratosthenes
    max_num = max(nums)
    primes = sieveOfEratosthenes(max_num)

    # Play each round of the game
    for n in nums:
        # Count prime numbers up to and including n
        prime_count = sum(primes[:n+1])

        # If the prime count is even, Ben wins; if odd, Maria wins
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def sieveOfEratosthenes(n):
    """
    Generates an array indicating whether numbers are prime,
    using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit of numbers to check for primality.

    Returns:
        list of bool: A list indicating whether each
        number up to n is prime.
    """
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is True, then it is a prime
        if prime[p]:
            # Updating all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # 0 and 1 are not prime numbers
    prime[0], prime[1] = False, False
    return prime


# Example usage
if __name__ == "__main__":
    x = 3
    nums = [10, 5, 6]
    winner = isWinner(x, nums)
    print(f"The winner is: {winner}")
