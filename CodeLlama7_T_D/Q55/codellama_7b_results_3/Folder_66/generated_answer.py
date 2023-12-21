
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate over the circular list and find contiguous integers that have a product equal to n
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sublist and its product
        current_sublist = [circular_list[i]]
        current_product = circular_list[i]

        # Iterate over the remaining elements in the circular list
        for j in range(i + 1, len(circular_list)):
            # If the product of the current sublist and the next element is equal to n, append the next element to the current sublist
            if current_product * circular_list[j] == n:
                current_sublist.append(circular_list[j])
                current_product = current_product * circular_list[j]

        # If the current sublist is not empty, append it to the list of sublists
        if len(current_sublist) > 0:
            sublists.append(current_sublist)

    # Return the list of sublists
    return sublists
