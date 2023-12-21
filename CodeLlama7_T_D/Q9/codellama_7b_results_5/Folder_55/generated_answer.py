
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the list
    for i in range(10, len(my_list)):
        if my_list[i] % 2 != 0:
            # Return the list of all odd integers from index 10 to index 10, both inclusive
            return [my_list[j] for j in range(10, i+1) if my_list[j] % 2 != 0]
    # If no odd integers exist in the specified range, return an empty list
    return []
