
def lists_with_product_equal_n(lst, n):
    # create an empty list to store the sublists
    sublists = []
    # loop through the elements of the given list
    for i in range(len(lst)):
        # get the current element and its product with n
        curr_elem = lst[i]
        prod_with_n = curr_elem * n
        # check if the product is equal to 247
        if prod_with_n == 247:
            # create a new list to store the sublist
            sublist = []

            # loop through the elements of the given list and append them to the sublist if their product with n is equal to 247
            for j in range(i, len(lst)):
                curr_elem = lst[j]
                prod_with_n = curr_elem * n
                if prod_with_n == 247:
                    sublist.append(curr_elem)

            # append the sublist to the list of sublists
            sublists.append(sublist)

    return sublists
