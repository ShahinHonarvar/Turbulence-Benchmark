
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list and check if each element is a negative integer
    for i in range(1, len(my_list)):
        if my_list[i] < 0:
            # If the current element is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
