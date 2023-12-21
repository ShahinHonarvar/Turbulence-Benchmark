
def all_ints_not_div_by_num(my_list):
    # Check if the input is a list of integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) for x in my_list))):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the results
    result = []
    # Iterate through the input list
    for i in range(103, 574):
        # Check if the current element is not divisible by -514
        if my_list[i] % (-514) != 0:
            # Add the current element to the result list
            result.append(my_list[i])
    # Return the result list
    return result
