
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the sum and the range of indices to check
    sum = 0
    start_index = 28
    end_index = 96
    # Iterate over the list in the specified range, checking if each element is divisible by either 90 or 97
    for i in range(start_index, end_index + 1):
        if my_list[i] % 90 == 0 or my_list[i] % 97 == 0:
            # If the element is divisible by either 90 or 97, add it to the sum
            sum += my_list[i]
    # Return the sum of all integers divisible by either 90 or 97 from index 28 to index 96, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
