
def find_divisors_in_range(n):
    # Initialize an empty list to store the divisors
    divisors = []

    # Iterate from 372 to 494, checking if each number is a divisor of n
    for i in range(372, 495):
        # If i is a divisor of n, add it to the list of divisors
        if n % i == 0:
            divisors.append(i)

    # Return the list of divisors found in the specified range
    return divisors
