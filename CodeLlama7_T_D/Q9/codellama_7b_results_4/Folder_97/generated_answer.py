
def all_odd_ints_inclusive(my_list):
    # Get the start and end indices of the specified range
    start = 40
    end = 80
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from the start index to the end index
    for i in range(start, end + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from the specified range, or an empty list if no such integers exist
    return odd_ints
