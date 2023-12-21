
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list and check if each integer is divisible by either -1 or 13
    for i in range(len(my_list)):
        if my_list[i] % -1 == 0 or my_list[i] % 13 == 0:
            # If the integer is divisible by either -1 or 13, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -1 or 13 from index 0 to index 5, both inclusive
    return sum
