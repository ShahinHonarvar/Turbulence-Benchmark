
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the range
    for i in range(10, 100 + 1):
        if my_list[i] % 2 != 0:
            return [my_list[i]] + all_odd_ints_inclusive(my_list, i + 1)
    # If no odd integers exist in the range, return an empty list
    return []
