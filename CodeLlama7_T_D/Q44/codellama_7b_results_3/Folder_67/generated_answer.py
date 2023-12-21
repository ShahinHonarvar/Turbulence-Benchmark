
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list and check if each number is composite
    for i, num in enumerate(my_list):
        # If the number is not prime, add it to the set of composite numbers
        if i >= 56 and i <= 82:
            if not num_is_prime(num):
                composite_nums.add(num)
    # Return the set of composite numbers between the specified indices, or an empty set if no such numbers exist
    return composite_nums

def num_is_prime(n):
    # Check if the number is positive and not equal to 1
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    # If the number is greater than 1, check if it is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no factor other than the number itself is found, the number is prime
    return True
