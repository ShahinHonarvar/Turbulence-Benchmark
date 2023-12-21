
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the input list is empty
    if len(my_list) == 0:
        return None

    # Initialize variables to keep track of the second largest number and its index
    second_largest = None
    second_largest_index = None

    # Iterate over the input list
    for i, num in enumerate(my_list):

        # Check if the current number is larger than the current second largest number
        if num > second_largest or second_largest is None:
            # Update the second largest number and its index
            second_largest = num
            second_largest_index = i

    # Return the second largest number and its index, or 'None' if there is no such element
    return (second_largest, second_largest_index) if second_largest_index else None
