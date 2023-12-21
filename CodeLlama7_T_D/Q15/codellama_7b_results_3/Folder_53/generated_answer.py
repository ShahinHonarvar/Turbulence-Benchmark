
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 300
    end_index = 300
    # Check if the list is empty or if the specified range is out of bounds
    if len(my_list) == 0 or start_index < 0 or end_index >= len(my_list):
        return sum

    # Iterate through the list and add up the odd integers in the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers in the specified range
    return sum
