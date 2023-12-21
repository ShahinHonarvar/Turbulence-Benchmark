
def find_second_largest_num(num_list):
    # check if the list has at least 35 elements
    if len(num_list) >= 35:
        # extract the subset of the list and find the second largest number
        subset = num_list[31:35]
        subset.sort(reverse=True)
        return subset[1]
    else:
        return None
