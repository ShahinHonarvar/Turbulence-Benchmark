
def find_sum_of_multiples(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The input must be a positive integer.")

    # Initialize the sum to 0
    sum = 0

    # Loop through the first 16 positive multiples of n
    for i in range(1, 17):
        sum += i * n

    return sum
