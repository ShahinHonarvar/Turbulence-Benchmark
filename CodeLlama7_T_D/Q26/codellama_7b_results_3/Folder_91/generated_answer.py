
def sum_in_range(my_list):
    # Initialize variables
    range_sum = 0
    my_list_copy = my_list[:]
    # Remove integers outside the range from the list copy
    for i in range(len(my_list_copy)):
        if not (-8 <= my_list_copy[i] <= 8):
            my_list_copy.pop(i)
    # Calculate the sum of the remaining integers
    for num in my_list_copy:
        range_sum += num
    return range_sum
