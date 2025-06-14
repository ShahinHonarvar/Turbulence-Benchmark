
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 300
    end_index = 300
    # Check if list is empty
    if not my_list:
        return sum

    # Check if indices are out of range
    if start_index < 0 or end_index > len(my_list) - 1:
        return sum

    # Iterate over odd integers in specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return sum of odd integers
    return sum
