
def lists_with_product_equal_n(circulat_list):
    # initialize an empty list to store the sublists
    sublists = []

    # loop through each element in the circular list
    for i in range(len(circulat_list)):

        # initialize a variable to store the product of the elements in the current sublist
        product = 1

        # loop through each element in the circular list starting from the current index
        for j in range(i, len(circulat_list)):

            # calculate the product of the elements in the current sublist
            product *= circulat_list[j]

            # if the product equals 25, add the current sublist to the list of sublists
            if product == 25:
                sublists.append(circulat_list[i:j+1])

    # return the list of sublists
    return sublists
