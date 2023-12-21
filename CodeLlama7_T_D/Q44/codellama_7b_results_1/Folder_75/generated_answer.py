
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the input list and check if each number is composite
    for i, num in enumerate(my_list):
        # If the number is not prime, add it to the set of composite numbers
        if i >= 75 and i <= 85:
            if not is_prime(num):
                composite_nums.add(num)
    return composite_nums
