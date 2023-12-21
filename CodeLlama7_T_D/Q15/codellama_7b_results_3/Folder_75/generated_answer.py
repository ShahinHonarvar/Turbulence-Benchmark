
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 56
    end_index = 57
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return sum

    # Loop through the list and calculate the sum of odd integers within the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    return sum
