
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the current element and its predecessor
        product = circular_list[i] * circular_list[(i + 1) % len(circular_list)]

        # If the product is equal to 99, add the sublist containing the current element to the list of sublists
        if product == 99:
            sublists.append([circular_list[i]])

        # If the product is not equal to 99, continue iterating over the elements of the circular list
        else:
            continue


    # Return the list of sublists found

    return sublists
