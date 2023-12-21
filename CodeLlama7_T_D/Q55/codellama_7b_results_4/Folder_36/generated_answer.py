
def lists_with_product_equal_n(circular_list):
    # Check if the given list is empty or None
    if circular_list == [] or circular_list == None:
        return []

    # Initialize an empty list to store the sublists
    sublists = []

    # Iterate through the given list and find contiguous integers whose product equals 714
    for i in range(len(circular_list))):
        current_product = 1
        current_sum = 0
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            current_sum += circular_list[j]
            if current_product == 714:
                sublists.append([current_sum])
                break

    # Return the list of sublists found in the given list
    return sublists
