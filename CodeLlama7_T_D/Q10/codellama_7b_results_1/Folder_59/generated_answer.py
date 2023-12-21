
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list of integers and check if each integer is odd
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
