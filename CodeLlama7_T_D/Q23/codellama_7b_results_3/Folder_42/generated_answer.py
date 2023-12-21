
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 1 to n, checking if each number is a divisor of n
    for i in range(1, n + 1):
        if n % i == 0 and 14 <= i <= 93:
            # If the current number is a divisor of n, add it to the list of divisors
            divisors.append(i)

    return divisors
