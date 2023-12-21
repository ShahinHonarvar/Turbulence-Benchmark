
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 86
    end_index = 89

    # Iterate through the list and calculate the sum of all integers divisible by either -61 or -79 from index 86 to index 89, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % -61 == 0 or my_list[i] % -79 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -61 or -79 from index 86 to index 89, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
