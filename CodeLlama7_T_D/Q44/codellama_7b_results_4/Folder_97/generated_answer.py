
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # If the current number is between index 15 and 39 (both inclusive)
        if 15 <= i <= 39:
            # Check if the current number is composite using the primality test
            if is_composite(my_list[i]):
                # If it is composite, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 15 and 39 (both inclusive), or an empty set if no such numbers exist
    return composite_nums

# Primality test to check if a number is composite
def is_composite(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
