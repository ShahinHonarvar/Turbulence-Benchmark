
def sum_even_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 82
    end_index = 86
    # Iterate through the list and find all even integers in the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
