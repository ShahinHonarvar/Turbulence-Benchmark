
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 86
    end_index = 90
    divisor_1 = -71
    divisor_2 = -67
    sum = 0

    # Iterate through the list and check if each integer is divisible by either -71 or -67
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor_1 == 0 or my_list[i] % divisor_2 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -71 or -67 from index 86 to index 90, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
