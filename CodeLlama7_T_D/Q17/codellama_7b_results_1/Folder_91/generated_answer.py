
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Loop through the list of integers and check if each integer is divisible by both 8 and -3
    for i in range(len(my_list)):
        if my_list[i] % 8 == 0 and my_list[i] % (-3) == 0:
            # If the current integer is divisible by both 8 and -3, append it to the list of divisible integers
            divisible_integers.append(my_list[i])
    return divisible_integers
