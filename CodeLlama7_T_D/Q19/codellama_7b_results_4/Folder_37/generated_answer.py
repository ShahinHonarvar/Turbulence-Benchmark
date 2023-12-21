
def all_ints_not_div_by_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Initialize an empty list to store the results
    result = []
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is not divisible by 5
        if i % 5 != 0:
            # Add the current integer to the results list
            result.append(i)
    # Return the results list
    return result
