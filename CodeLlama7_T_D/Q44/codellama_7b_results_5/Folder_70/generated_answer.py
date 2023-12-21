
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(32, 36):
        # Check if the number at index i is composite
        if is_composite(my_list[i]):
            # If it is composite, add it to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n without leaving a remainder, return False
            if n % i == 0:
                return False

    # If we reach this point, the number is either prime or a composite number that is not divisible by any prime number less than or equal to its square root. In either case, return True.
    return True
