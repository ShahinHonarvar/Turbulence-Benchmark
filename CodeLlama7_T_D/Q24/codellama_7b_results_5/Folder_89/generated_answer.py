
def sum_of_divisors_in_range(n):
    # Check if n is positive and between 14 and 48 (both inclusive)
    if not (n > 0 and 14 <= n <= 48):
        return 0

    # Initialize the sum to 0

    sum = 0

    # Iterate over the divisors of n between 14 and 48 (both inclusive)

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i

            if i * i < n:
                sum += n // i

    # Return the sum of the divisors of n between 14 and 48 (both inclusive)

    return sum
