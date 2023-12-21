
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_list = []

    # Iterate through the list of integers and check if each integer is divisible by -40
    for i in range(75, 86):
        if my_list[i] % -40 == 0:
            # If the integer is divisible by -40, append it to the list of divisible integers
            div_list.append(my_list[i])

    return div_list
