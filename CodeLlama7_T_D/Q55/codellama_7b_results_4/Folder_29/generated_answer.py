
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list

    for i in range(len(circular_list)):

        # Initialize variables to keep track of the current sublist and its product

        current_sublist = []

        current_product = 1


        # Add the current element to the current sublist and update the product

        current_sublist.append(circular_list[i])

        current_product *= circular_list[i]


        # Iterate over the remaining elements of the circular list

        for j in range(i + 1, len(circular_list)):

            # Add the current element to the current sublist and update the product

            current_sublist.append(circular_list[j])

            current_product *= circular_list[j]


            # If the product of the current sublist is equal to 15, add it to the list of sublists and reset the variables

            if current_product == 15:

                sublists.append(current_sublist)

                current_sublist = []

                current_product = 1


    # Return the list of sublists


    return sublists
