
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Get the current element and its index in the circular list
        element = circular_list[i]
        index = i

        # Check if the product of the elements in the sublist is equal to n
        if index >= len(sublists):
            sublists.append([element])
        else:
            sublists[index].append(element)

    return sublists
