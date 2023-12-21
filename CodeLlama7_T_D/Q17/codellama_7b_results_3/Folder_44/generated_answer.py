
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list and check if each integer is divisible by both 74 and 15
    for i in range(25, 70 + 1):
        if my_list[i] % 74 == 0 and my_list[i] % 15 == 0:
            div_ints.append(my_list[i])

    # Return the list of divisible integers
    return div_ints
