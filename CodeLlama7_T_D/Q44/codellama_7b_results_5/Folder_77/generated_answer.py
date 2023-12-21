
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list and check if each element is a prime number
    for i in range(667, 774 + 1):
        if not my_list[i - 1] in composite_nums:
            # If the element is not a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i - 1])
    return composite_nums
