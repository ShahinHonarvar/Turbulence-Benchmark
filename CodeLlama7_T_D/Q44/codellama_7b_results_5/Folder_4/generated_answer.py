
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(56, 98+1):
        # Check if the number is composite using the function is_composite()
        if is_composite(my_list[i]):
            # If the number is composite, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 56 to index 98, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n-1
        for i in range(2, n):
            # If the remainder of dividing n by i is 0, return False (n is not composite)
            if n % i == 0:
                return False

    # Return True (n is composite)
    return True
