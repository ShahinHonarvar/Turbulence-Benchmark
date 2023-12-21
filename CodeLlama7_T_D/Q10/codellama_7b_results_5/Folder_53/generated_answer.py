
def all_odd_ints_exclusive(my_list):
    # Define start and end indices for the range of odd integers
    start = 100
    end = 101
    # Initialize an empty list to store the result
    result = []
    # Iterate over the list and append odd integers to the result
    for i in range(start, end):
        if my_list[i] % 2 != 0:
            result.append(my_list[i])
    return result
