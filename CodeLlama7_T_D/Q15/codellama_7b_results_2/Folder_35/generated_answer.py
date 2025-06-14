
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 30
    end_index = 48
    # Check if the list is empty or has fewer than 30 elements
    if len(my_list) == 0 or len(my_list) < 30:
        return sum

    # Iterate over the list and sum up the odd integers in the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers in the specified range
    return sum
