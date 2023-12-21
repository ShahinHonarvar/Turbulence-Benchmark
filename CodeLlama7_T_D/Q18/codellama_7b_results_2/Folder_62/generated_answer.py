
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices
    sum = 0
    start_idx = 44
    end_idx = 59
    # Iterate over the range of indices and check if each integer is divisible by either 39 or 15
    for i in range(start_idx, end_idx + 1):
        if my_list[i] % 39 == 0 or my_list[i] % 15 == 0:
            sum += my_list[i]
    return sum
