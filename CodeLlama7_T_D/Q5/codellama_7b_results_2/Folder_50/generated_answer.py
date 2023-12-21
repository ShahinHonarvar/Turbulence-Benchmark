
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list and check if each element is a negative integer
    for i in range(70, 85):
        if my_list[i] < 0:
            # If the element is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 70 to index 84, both inclusive
    return neg_ints
