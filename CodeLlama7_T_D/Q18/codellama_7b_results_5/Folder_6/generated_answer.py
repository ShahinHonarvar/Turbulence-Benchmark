
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range and the sum
    start = 41
    end = 56
    sum = 0

    # Loop through the range and calculate the sum of all integers divisible by either 82 or 90
    for i in range(start, end + 1):
        if my_list[i] % 82 == 0 or my_list[i] % 90 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either 82 or 90 from index 41 to index 56, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
