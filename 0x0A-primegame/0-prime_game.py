#!/usr/bin/python3
"""Prime Game: A game where players compete to remove
    prime numbers and their multiples"""


def isWinner(num_rounds, round_limits):
    """
    Determines the winner of the prime game.

    Args:
        num_rounds (int): The number of rounds played.
        round_limits (list of int): A list containing the upper
        limits of consecutive integers for each round.

    Returns:
        str or None: The name of the player who won the most rounds.
        Returns 'Maria' or 'Ben' if a winner is determined, or
        None if the winner cannot be determined.
    """

    round_wins = {'Maria': 0, 'Ben': 0}

    for round_idx in range(num_rounds):
        round_winner = determine_round_winner(
                round_limits[round_idx], num_rounds)
        if round_winner is not None:
            round_wins[round_winner] += 1

    if round_wins['Maria'] > round_wins['Ben']:
        return 'Maria'
    elif round_wins['Ben'] > round_wins['Maria']:
        return 'Ben'
    else:
        return None


def determine_round_winner(round_limit, num_rounds):
    '''
    Determines the winner of a single round of the prime game.

    Args:
        round_limit (int): The upper limit of consecutive
        integers for the current round.
        num_rounds (int): The total number of rounds played.

    Returns:
        str or None: The name of the player who won the round.
        Returns 'Maria' or 'Ben' if a winner is determined, or
        None if the winner cannot be determined.
    '''

    remaining_numbers = [i for i in range(1, round_limit + 1)]
    players = ['Maria', 'Ben']

    for num_idx in range(round_limit):
        current_player = players[num_idx % 2]
        selected_indices = []
        prime_number = -1
        for idx, num in enumerate(remaining_numbers):
            if prime_number != -1:
                if num % prime_number == 0:
                    selected_indices.append(idx)
            else:
                if is_prime(num):
                    selected_indices.append(idx)
                    prime_number = num
        if prime_number == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_indices):
                del remaining_numbers[val - idx]
    return None


def is_prime(number):
    '''
    Checks if a number is prime.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    '''

    # 0, 1, and even numbers greater than 2 are NOT PRIME
    if number < 2 or number % 2 == 0 and number > 2:
        return False
    else:
        # A number is not prime if it is divisible by another
        # number less than or equal to its square root
        for i in range(3, int(number**(1/2)) + 1, 2):
            if number % i == 0:
                return False
        return True
