
def lists_with_product_equal_n(circular_list, n):
    # Initialize an empty list to store the sublists
    sublists = []
    # Iterate over the elements of the circular list
    for i in range(len(circular_list)):
        # Extract a contiguous subsequence from the circular list
        subsequence = circular_list[i:] + circular_list[:i]
        # Check if the product of the elements in the subsequence is equal to n
        if all(element * subsequence[j] == n for j in range(len(subsequence)))):
            # Add the subsequence to the list of sublists
            sublists.append(subsequence)
    return sublists
