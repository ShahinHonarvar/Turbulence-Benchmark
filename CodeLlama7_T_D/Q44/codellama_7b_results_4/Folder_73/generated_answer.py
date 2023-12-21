
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(28, 41):
        # Check if the number at index i is composite
        if is_composite(my_list[i]):
            # If it is composite, add it to the set
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 28 to index 40, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums

# A function to check if a number is composite or not
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If i divides n with no remainder, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, either n is a prime number or it is not a prime number
    return True
