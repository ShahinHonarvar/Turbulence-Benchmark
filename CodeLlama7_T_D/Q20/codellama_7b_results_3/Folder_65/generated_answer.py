
def find_n_th_smallest_num(my_list, n):
    # Check if input list is valid
    if not my_list or len(my_list) < n:
        raise ValueError("Input list must be valid and contain at least the specified number of elements")
    # Sort the input list in ascending order
    my_list.sort()
    # Return the n-th smallest element from the sorted list
    return my_list[n - 1]
