
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the results
    result = []
    # Iterate over the list, starting at index 60
    for i in range(len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the result list
            result.append(my_list[i])
    return result
