
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list and check if each integer is divisible by both 275 and 580
    for i in range(154, 799 + 1):
        if my_list[i] % 275 == 0 and my_list[i] % 580 == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 275 and 580 from index 154 to index 798, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
