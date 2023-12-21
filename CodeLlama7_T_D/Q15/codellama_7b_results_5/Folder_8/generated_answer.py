
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 23
    end_index = 23
    # Check if the list is empty or has less than 24 elements
    if len(my_list) == 0 or len(my_list) < 24:
        return sum

    # Iterate through the list, starting from the 23rd index and ending at the 23rd index
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    return sum
