
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the elements of the circular list
    for i in range(len(my_list)):

        # Initialize a variable to store the product of the current element and its successor
        prod = my_list[i] * my_list[(i+1)%len(my_list)]

        # If the product is equal to -18, add the current element and its successor to the list of sublists
        if prod == -18:
            sublists.append([my_list[i], my_list[(i+1)%len(my_list)]]))

    # Return the list of sublists
    return sublists
