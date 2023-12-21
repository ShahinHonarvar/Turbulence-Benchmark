
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list and check if each integer is divisible by both 2 and 3
    for i in range(7, len(my_list)):
        if my_list[i] % 2 == 0 and my_list[i] % 3 == 0:
            # If the integer is divisible by both 2 and 3, add it to the list of divisible integers
            divisible_ints.append(my_list[i])
    return divisible_ints
