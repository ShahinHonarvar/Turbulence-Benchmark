
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the input list and check if each element is a positive integer
    for i in range(20, 200):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
