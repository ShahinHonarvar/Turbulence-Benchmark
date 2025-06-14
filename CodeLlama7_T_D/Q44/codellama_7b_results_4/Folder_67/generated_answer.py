
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each number is composite between indices 56 and 82
    for i in range(len(my_list)):
        # Check if the current number is between indices 56 and 82
        if 56 <= i <= 82:
            # Check if the current number is prime
            if is_prime(my_list[i]):
                # If the current number is prime, add it to the set of composite numbers
                composite_numbers.add(my_list[i])

    # Return the set of composite numbers between indices 56 and 82
    return composite_numbers

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n, return False
            if n % i == 0:
                return False

    # If n is a prime number, return True
    return n > 1
