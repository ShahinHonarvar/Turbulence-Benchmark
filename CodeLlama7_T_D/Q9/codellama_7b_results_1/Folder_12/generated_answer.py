
def all_odd_ints_inclusive(my_list):
    # Define the start and end indices for the range of odd integers
    start = 14
    end = 64
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the list from start to end, checking if each element is odd
    for i in range(start, end+1):
        if my_list[i] % 2 != 0:
            # If the element is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 14 to index 64, both inclusive
    return odd_ints
