
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    prod = 1
    for i in circular_list:
        prod *= i

    # Initialize a list to store the sublists

    sublists = []

    # Iterate over the list and find contiguous sublists whose product is equal to n

    for i in range(len(circular_list)):

        # Initialize variables to keep track of the current sublist and its product

        current_sublist = [circular_list[i]]
        current_product = prod / circular_list[i]

        # Iterate over the remaining elements in the list

        for j in range(i + 1, len(circular_list)):

            # If the product of the current sublist and the next element is equal to n, add the sublist to the list of sublists

            if current_product == n:
                sublists.append(current_sublist)

            # Add the next element to the current sublist

            current_sublist.append(circular_list[j])

            # Update the product of the current sublist

            current_product *= circular_list[j]

    return sublists
