
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the given list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the current element and its successor
        prod = my_list[i] * my_list[(i+1) % len(my_list)]

        # If the product is equal to -41, add the current element and its successor to the sublists list
        if prod == -41:
            sublists.append([my_list[i], my_list[(i+1) % len(my_list)]]])

    # Return the sublists list

    return sublists
