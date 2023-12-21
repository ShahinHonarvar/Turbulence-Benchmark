
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    nums_to_check = [-9, -3]
    # Iterate through the list and check if each integer is divisible by either -9 or -3
    for i in range(1, 8):
        if my_list[i] % nums_to_check[0] == 0 or my_list[i] % nums_to_check[1] == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either -9 or -3 from index 1 to index 8, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
