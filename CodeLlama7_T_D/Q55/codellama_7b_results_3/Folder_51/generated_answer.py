
def lists_with_product_equal_n(circular_list):
    # create a copy of the circular list
    temp = circular_list[:]
    # initialize an empty list to store the sublists
    sublists = []
    # loop through the elements of the circular list
    for i in range(len(temp)):
        # initialize variables to keep track of the current sublist and its product
        current_sublist = [temp[i]]
        product = temp[i]
        # loop through the remaining elements of the circular list
        for j in range(i+1, len(temp)):
            # if the product of the two elements is equal to -44, add them to the current sublist
            if (temp[j] * product) == -44:
                current_sublist.append(temp[j])
                product = temp[j] * product
            # if the product of the two elements is not equal to -44, break out of the loop
            else:
                break

        # if the current sublist is not empty, add it to the list of sublists
        if len(current_sublist) > 0:
            sublists.append(current_sublist)

    # return the list of sublists
    return sublists
