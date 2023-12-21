
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 34
    end_index = 55
    # Iterate through list and add odd integers to sum
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return sum
