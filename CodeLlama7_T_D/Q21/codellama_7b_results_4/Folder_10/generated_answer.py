
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the list of integers and check if each integer is divisible by -59
    for i in range(42, 89 + 1):
        if my_list[i] % -59 == 0:
            # If the integer is divisible by -59, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    return divisible_integers
