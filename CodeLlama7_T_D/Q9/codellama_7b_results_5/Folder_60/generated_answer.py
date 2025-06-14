
def all_odd_ints_inclusive(my_list):
    # Get the length of the list
    list_length = len(my_list)
    # Define the start and end indices for the range
    start_index = 75
    end_index = 85
    # Check if the specified range is valid
    if start_index >= list_length or end_index < 0:
        return []

    # Get all odd integers within the specified range
    odd_ints = [my_list[i] for i in range(start_index, end_index + 1) if my_list[i] % 2 != 0]

    return odd_ints
