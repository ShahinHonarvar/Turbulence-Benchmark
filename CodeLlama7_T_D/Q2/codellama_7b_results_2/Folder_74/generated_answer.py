
def all_ints_exclusive(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Get the length of the list
    list_length = len(my_list)

    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the elements of the input list
    for i in range(32, list_length):
        # Add each element to the result list
        result_list.append(my_list[i])

    # Return the result list
    return result_list
