
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    for i in range(20, len(my_list)):
        if my_list[i] % 2 != 0:
            # Return the list of all odd integers in the range
            return [my_list[j] for j in range(i+1, len(my_list)) if my_list[j] % 2 != 0]
    # If no odd integers exist in the specified range, return an empty list
    return []
