
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list and check if each number is composite
    for i in range(len(my_list))):
        num = my_list[i]
        if (num > 1) and (any(num % x == 0 for x in range(2, int(num ** 0.5) + 1)))):
            composite_nums.add(num)
    # Return the set of all composite numbers in the specified range
    return composite_nums
