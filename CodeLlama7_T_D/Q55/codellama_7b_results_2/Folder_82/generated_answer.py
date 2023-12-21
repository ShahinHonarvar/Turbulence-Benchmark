
def lists_with_product_equal_n(circular_list):
    # Create a set of all possible sublists
    sublists = []
    for i in range(len(circular_list)):
        # Get the current element and its neighbors
        curr_element = circular_list[i]
        prev_element = None
        if i > 0:
            prev_element = circular_list[i - 1]
        next_element = None
        if i < len(circular_list) - 1:
            next_element = circular_list[i + 1]
        # Check if the current element and its neighbors form a sublist with product equal to n
        if curr_element * prev_element * next_element == n:
            sublists.append([curr_element, prev_element, next_element])
    return sublists
