
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list and check if each integer is divisible by 77
    for i in range(66, 82):
        if my_list[i] % 77 == 0:
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by 77 from index 66 to index 81, both inclusive
    return div_ints
