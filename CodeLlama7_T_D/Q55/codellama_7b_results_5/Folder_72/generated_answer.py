
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the circular list and find contiguous integers with a product equal to 10
    for i in range(len(circular_list)):
        # Initialize variables to keep track of the current sublist and its product
        curr_sublist = [circular_list[i]]
        curr_product = circular_list[i]

        # Iterate through the remaining elements in the circular list
        for j in range(i + 1, len(circular_list)):
            # If the product of the current sublist and the next element is equal to 10, add the next element to the current sublist
            if curr_product * circular_list[j] == 10:
                curr_sublist.append(circular_list[j])
                curr_product = curr_product * circular_list[j]

        # If the current sublist has at least one element, add it to the list of sublists
        if len(curr_sublist) > 0:
            sublists.append(curr_sublist)

    # Return the list of sublists
    return sublists
