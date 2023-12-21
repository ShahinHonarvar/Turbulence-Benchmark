
def lists_with_product_equal_n(circular_list):
    # initialize an empty list to store the sublists
    sublists = []

    # loop through the elements of the circular list
    for i in range(len(circular_list)):

        # initialize a variable to store the current element and its index
        curr_elem = circular_list[i]
        curr_idx = i

        # initialize variables to store the product and the sublist
        product = 1
        sublist = []

        # loop through the elements of the circular list starting from the current element
        for j in range(curr_idx, len(circular_list)):

            # calculate the product of the current element and its successor
            product *= circular_list[j]

            # if the product is equal to 43, add the sublist to the list of sublists
            if product == 43:
                sublist.append(curr_elem)
                sublist.extend(circular_list[curr_idx + 1:j])
                sublists.append(sublist)

                # break out of the inner loop and start a new one with the next element as the current element
                break

            # if the product is greater than 43, exit the inner loop
            elif product > 43:
                break

        # if the product is not equal to 43 after looping through all the elements of the circular list starting from the current element, continue with the next element as the current element
        if product != 43:
            continue

        # if a sublist has been found with a product equal to 43, break out of the outer loop
        break

    # return the list of sublists each of which contains the contiguous integers from the given circular list such that their product equals 43
    return sublists
