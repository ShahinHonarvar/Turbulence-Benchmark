
def all_ints_div_by_num(my_list):
    # create a new list to store the divisible integers
    divisible_ints = []

    # loop through the list and check if each integer is divisible by -97

    for i in range(len(my_list)):
        if my_list[i] % -97 == 0:
            # if the integer is divisible by -97, add it to the new list

            divisible_ints.append(my_list[i])

    return divisible_ints
