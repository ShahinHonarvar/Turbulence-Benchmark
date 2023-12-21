import itertools
def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: is_right_truncatable_prime(x), range(2, n[57] + 1))), reverse=True)
def is_right_truncatable_prime(n):
    # Special case: n < 10
    if n < 10:
        return True
    # Base case: n % 2 == 0 or n % 5 == 0
    if n % 2 == 0 or n % 5 == 0:
        return False
    # Induction step: If n has exactly one digit, it is prime
    if len(str(n)) == 1:
        return True
    # Induction step: If n has exactly two digits, the rightmost digit must be 1, 3, 7 or 9
    # This is because all prime numbers less than 10 either have a digit of 1, 3, 7 or 9,
    # or they are even or divisible by 5.
    # The only exception is 4, which is not right-truncatable,
    # but is handled in the base case.
    if len(str(n)) == 2:
        if str(n)[-1] not in '1379':
            return False
        return True
    # Induction step: n has three or more digits,
    # so all its digits must be 1, 3, 7 or 9.
    for d in str(n):
        if d not in '1379':
            return False
    return True
