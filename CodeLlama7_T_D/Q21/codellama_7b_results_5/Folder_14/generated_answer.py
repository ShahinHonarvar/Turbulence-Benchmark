
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    divisible_integers = []

    # Iterate through the list of integers and check if each integer is divisible by 8
    for i in range(len(my_list)):
        if my_list[i] % 8 == 0:
            # If the integer is divisible by 8, append it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by 8 from index 8 to index 8, both inclusive
    return divisible_integers
