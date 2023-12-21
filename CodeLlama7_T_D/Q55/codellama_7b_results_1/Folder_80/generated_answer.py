
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list

    for i in range(len(circular_list)):
        # Calculate the product of the elements in the current sublist

        prod = 1

        for j in range(i, len(circular_list)):
            prod *= circular_list[j]

            # If the product equals 43, add the sublist to the list of sublists and break out of the inner loop

            if prod == 43:
                sublists.append(circular_list[i:j + 1])

                break


    return sublists
