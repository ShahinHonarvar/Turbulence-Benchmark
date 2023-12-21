
def lists_with_product_equal_n(circular_list):

    sublists = []
    n = len(circular_list)

    # Iterate through all possible sublist lengths
    for length in range(1, n + 1):
        # Iterate through all possible starting indices
        for start in range(n):
            # Get the sublist of current length
            sublist = circular_list[start:start + length]
            # Check if the product of sublist is equal to zero
            if not sublist or 0 in sublist:
                sublists.append(sublist)

    return sublists
