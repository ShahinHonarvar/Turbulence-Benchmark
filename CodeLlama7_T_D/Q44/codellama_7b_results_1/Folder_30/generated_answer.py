
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Invalid input. The input must be a list of positive integers.")
    # Define the range of indices to search for composite numbers
    start_index = 19
    end_index = 92
    # Initialize an empty set to store the composite numbers found in the specified range
    composite_nums = set()
    # Iterate over the list and check if each element is a composite number between the defined indices
    for i, num in enumerate(my_list):
        if start_index <= i < end_index:
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composite_nums.add(num)
    # Return the set of composite numbers found in the specified range
    return composite_nums
