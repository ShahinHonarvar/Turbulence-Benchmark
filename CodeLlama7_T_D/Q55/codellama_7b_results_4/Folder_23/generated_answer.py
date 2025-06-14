
def lists_with_product_equal_n(circular_list):
    # create an empty list to store the sublists
    sublists = []

    # loop through the elements of the circular list
    for i in range(len(circular_list)):

        # initialize a variable to store the product of the elements in the sublist
        product = 1

        # loop through the elements of the circular list starting from the current element
        for j in range(i, len(circular_list)):

            # multiply the elements of the sublist
            product *= circular_list[j]

            # if the product equals -95, add the sublist to the list of sublists and break out of the loop
            if product == -95:
                sublists.append(circular_list[i:j+1])
                break

    # return the list of sublists
    return sublists
