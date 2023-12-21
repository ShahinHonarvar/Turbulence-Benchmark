
def lists_with_product_equal_n(circular_list):
    # initialize an empty list to store the sublists
    sublists = []

    # loop through each element in the circular list
    for i in range(len(circular_list)):

        # initialize a variable to store the current product
        current_product = 1

        # initialize a variable to store the current size of the sublist
        current_size = 0

        # loop through each element in the circular list starting from the current index
        for j in range(i, len(circular_list)):

            # update the product and size of the sublist
            current_product *= circular_list[j]
            current_size += 1

            # check if the product equals 96
            if current_product == 96:

                # add the sublist to the list of sublists
                sublists.append(circular_list[i:j+1])

                # break out of the inner loop since we have found a sublist that meets our requirements
                break

            # check if the size of the sublist exceeds the size of the given list
            elif current_size > len(circular_list):

                # break out of the outer loop since we have exhausted all possible sublists in the circular list
                break

    # return the list of sublists
    return sublists
