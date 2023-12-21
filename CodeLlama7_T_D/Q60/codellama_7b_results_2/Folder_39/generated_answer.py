
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    for i in range(2, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)
    return prime_numbers
```
Here is a possible implementation of the `is_prime` function:
```
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True
```
Here is a possible implementation of the `is_left_right_truncatable_prime` function:
```
def is_left_right_truncatable_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return False

    # Check if the number is left-and-right-truncatable prime number
    leading_leftmost_digit = int(str(n)[0])
    last_rightmost_digit = int(str(n))[-1]

    if n % leading_leftmost_digit == 0:
        return False

    if n % last_rightmost_digit == 0:
        return False

    return True
