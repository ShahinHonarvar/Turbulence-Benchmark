
def lists_with_product_equal_n(my_list):
    # Check if the product of all elements in the list is equal to -97
    if sum(my_list) == -97:
        return [my_list]
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements in the list
    for i in range(len(my_list)):
        # Check if the product of the current element and the next element is equal to -97
        if my_list[i] * my_list[(i + 1) % len(my_list)] == -97:
            # Add the current element to the sublist
            sublists.append([my_list[i]])
            # Add the next element to the sublist
            sublists[-1].append(my_list[(i + 1) % len(my_list))])
            # Check if the product of all elements in the sublist is equal to -97
            if sum(sublists[-1]) == -97:
                return [sublists[-1]]

    # If no such sublist exists, return an empty list
    return []
