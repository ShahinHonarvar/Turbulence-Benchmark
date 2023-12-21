
def lists_with_product_equal_n(lst):
    # Check if the list is empty
    if not lst:
        return []

    # Create an empty list to store the sublists
    sublists = []

    # Initialize variables for keeping track of the current product and its length
    curr_product = 1
    curr_length = 0

    # Iterate through the list
    for i in range(len(lst)):

        # Update the current product and its length
        curr_product *= lst[i]
        curr_length += 1

        # Check if the current product is equal to n
        if curr_product == n:
            sublists.append(lst[i-curr_length+1:i+1])

    return sublists
