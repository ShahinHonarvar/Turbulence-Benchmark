
def all_odd_ints_inclusive(my_list):
    # Get the range of odd integers in the list
    start = 43
    end = 86
    # Create an empty list to store the results
    result = []

    # Iterate over the range of indices and check if each index contains an odd integer

    for i in range(start, end + 1):
        if my_list[i] % 2 != 0:
            # If the current index contains an odd integer, add it to the result list
            result.append(my_list[i])

    return result
