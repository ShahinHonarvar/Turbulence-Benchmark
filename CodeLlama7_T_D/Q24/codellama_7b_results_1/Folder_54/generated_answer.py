
def sum_of_divisors_in_range(n):
    # Initialize the sum to 0
    sum = 0

    # Check if n is between 36 and 93, both inclusive
    if n >= 36 and n <= 93:

        # Iterate from 2 to sqrt(n)
        for i in range(2, int(n ** 0.5) + 1):

            # Check if i is a divisor of n
            if n % i == 0:

                # Add i to the sum
                sum += i

                # If i*i > n, there are no more factors to consider
                if i * i > n:
                    break

        # Return the sum of all positive divisors of n between 36 and 93, inclusive
        return sum

    # If n is not between 36 and 93, return 0
    else:
        return 0
