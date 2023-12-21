
def all_odd_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 43

    # Find the ending index of the range
    end_index = 51

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list and append odd integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
