
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0

    # Loop through the list and check if each element is divisible by either 11 or -7
    for i in range(len(my_list)):
        if my_list[i] % 11 == 0 or my_list[i] % -7 == 0:
            # If the element is divisible by either 11 or -7, add it to the sum
            sum += my_list[i]

    # Return the sum

    return sum
