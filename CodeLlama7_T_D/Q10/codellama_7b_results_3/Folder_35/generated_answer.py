
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    for i in range(10, 80):
        if my_list[i] % 2 != 0:
            first_odd = my_list[i]
            break

    # If no odd integers exist in the range, return an empty list
    if first_odd == None:
        return []

    # Find all odd integers in the range

    for i in range(10, 80):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    return odd_ints
