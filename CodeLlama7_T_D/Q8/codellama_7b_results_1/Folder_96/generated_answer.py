
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(50, len(my_list), 2):
        if my_list[i] % 2 == 0:
            # Start searching for even integers from index 50 to index 200, both exclusive
            for j in range(i + 1, 200, 2):
                if my_list[j] % 2 == 0:
                    return [my_list[i], my_list[j]]
            # If no even integers exist in the specified range, return an empty list
            return []
