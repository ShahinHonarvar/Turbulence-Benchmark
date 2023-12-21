
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 26 and 52 (inclusive)
        if i >= 26 and i <= 52:
            # Use the 'is_prime' function to check if the current number is a prime or composite number
            if not is_prime(my_list[i]):
                # If the current number is a composite number, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 26 and 52 (inclusive), or an empty set if no such composite numbers exist
    return composite_nums

# Define a function to check if a number is prime
def is_prime(n):
    # Check if 'n' is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of 'n'
        for i in range(2, int(n ** 0.5) + 1):
            # If 'i' divides 'n', return False
            if n % i == 0:
                return False

    # If we reach this point, return True (since n is either a prime number or is not divisible by any prime number less than or equal to its square root)
    return True
