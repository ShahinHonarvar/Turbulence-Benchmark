
def lists_with_product_equal_n(my_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Loop through each element in the input list
    for i in range(len(my_list)):
        # Initialize a variable to store the product of the current element and its successor
        prod = my_list[i] * my_list[(i+1) % len(my_list)]
        # If the product is equal to 537, add the current sublist to the output list
        if prod == 537:
            sublists.append([my_list[i], my_list[(i+1) % len(my_list)]]))
    return sublists
