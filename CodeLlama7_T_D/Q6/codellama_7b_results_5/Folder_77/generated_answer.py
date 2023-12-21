
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list and check if each element is a negative integer
    for i in range(111, 473):
        if my_list[i] < 0:
            # If the element is a negative integer, append it to the neg_ints list
            neg_ints.append(my_list[i])
    return neg_ints
