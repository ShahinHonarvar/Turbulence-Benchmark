
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 31

    for i in range(len(my_list)):
        if my_list[i] % 31 == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 31 from index 38 to index 55, both inclusive

    return divisible_ints
