
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list from index 7 to index 7, both inclusive
    for i in range(7, len(my_list)):
        # If the current element is divisible by either 5 or 7, add it to the sum
        if my_list[i] % 5 == 0 or my_list[i] % 7 == 0:
            sum += my_list[i]

    # Return the sum

    return sum
