
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    for i in range(50, len(my_list)):
        if my_list[i] % 2 != 0:
            # Return the list of all odd integers from index 50 to index 200, both exclusive
            return [my_list[j] for j in range(i + 1, 200, 2)]
    # If no odd integers exist in the specified range, return an empty list
    return []
