def all_left_truncatable_prime(n):
    res = []
    for x in range(3, n[2] + 1):
        if is_left_truncatable_prime(x):
            res.append(x)
    return res
def is_left_truncatable_prime(x):
    # Check if x is prime
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    # Check if all leftmost digits are prime
    for d in range(1, len(str(x)) + 1):
        # Check if current digit is 0
        if str(x)[-1 - d] == '0':
            return False
        # Check if current digit is prime
        if not is_prime(int(str(x)[-1 - d])):
            return False
    return True
def is_prime(x):
    # Check if x is prime
    if x < 2:
        return False
    # Check if x is a prime number
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    # Check if x is a prime number
    # Check only for odd numbers
    # Check if the square of the number is greater than the number
    if x < 4:
        return False
    if x % 2 == 0 or x % 3 == 0:
        return False
    # Check if x is prime
    # Check if x is a prime number
    # Check only for odd numbers
    # Check if the square of the number is greater than the number
    # Check if x is a prime number
    # Check only for odd numbers
    # Check if the square of the number is greater than the number
    return True
