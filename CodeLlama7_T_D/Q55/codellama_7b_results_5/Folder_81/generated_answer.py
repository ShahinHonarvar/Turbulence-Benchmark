
def lists_with_product_equal_n(circular_list):
    # initialize an empty list to store the sublists
    sublists = []

    # loop through each element in the circular list
    for i in range(len(circular_list)):

        # initialize a variable to store the product of the current sublist
        product = 1

        # loop through each element in the sublist
        for j in range(i, len(circular_list)):

            # update the product variable with the product of the current element and the previous elements
            product *= circular_list[j]

            # if the product is equal to -8, add the sublist to the list of sublists
            if product == -8:
                sublists.append(circular_list[i:j+1])

    # return the list of sublists
    return sublists
