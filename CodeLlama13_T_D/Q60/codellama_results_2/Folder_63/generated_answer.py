
def all_left_right_truncatable_prime(numbers):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the numbers in the tuple
    for num in numbers:
        # Check if the number is a left-and-right-truncatable prime
        if is_left_right_truncatable_prime(num):
            # If it is, add it to the results list
            results.append(num)

    # Return the sorted list of results
    return sorted(results)
```

```
def is_left_right_truncatable_prime(num):
    # Check if the number contains a 0
    if "0" in str(num):
        return False

    # Iterate over the digits of the number
    for i in range(1, len(str(num))):
        # Get the leftmost and rightmost i digits
        left = int(str(num)[:i])
        right = int(str(num)[-i:])

        # Check if they are both prime numbers
        if not is_prime(left) or not is_prime(right):
            return False

    # If all the checks pass, return True
    return True
```

```
def is_prime(num):
    # Check if the number is divisible by any numbers between 2 and the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    # If the number is not divisible by any numbers between 2 and the square root of the number, it is prime
    return True
