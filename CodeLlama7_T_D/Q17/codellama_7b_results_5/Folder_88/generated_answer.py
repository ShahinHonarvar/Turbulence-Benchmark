
def all_ints_div_by_both_two_nums(my_list):
    # Find the indices of the elements divisible by both 6 and 1
    indices = []
    for i in range(3, 9 + 1):
        if my_list[i] % 6 == 0 and my_list[i] % 1 == 0:
            indices.append(i)
    # Return the list of all integers divisible by both 6 and 1 from index 3 to index 9, both inclusive
    return [my_list[i] for i in indices]
