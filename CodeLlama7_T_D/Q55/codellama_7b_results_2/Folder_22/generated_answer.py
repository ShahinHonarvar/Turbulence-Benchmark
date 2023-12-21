
def lists_with_product_equal_n(lst):
    # Initialize an empty list to store the sublists
    sublists = []
    # Loop through each element in the input list
    for i in range(len(lst)):
        # Get the current element and its index
        current_element = lst[i]
        current_index = i
        # Initialize a variable to store the product of the current sublist
        product = 1
        # Loop through each element in the input list starting from the current index
        for j in range(current_index, len(lst)):
            # Get the current element and its index
            current_element = lst[j]
            current_index = j
            # Calculate the product of the current sublist
            product *= current_element
            # Check if the product equals 4
            if product == 4:
                # Add the current sublist to the list of sublists
                sublists.append(lst[i:j+1])
    return sublists
