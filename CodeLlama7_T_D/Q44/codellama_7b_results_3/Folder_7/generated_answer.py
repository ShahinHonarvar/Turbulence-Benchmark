
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list from index 527 to index 538, both inclusive
    for i in range(527, 539):
        # Check if the number at the current index is composite
        if is_composite(my_list[i]):
            # If it is composite, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 527 to index 538, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_numbers

def is_composite(n):

    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True
