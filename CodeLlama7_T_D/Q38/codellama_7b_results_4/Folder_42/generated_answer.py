
def find_subset_of_length_n(my_set):
    total = 0
    for i in range(len(my_set)):
        subset = my_set[i:]
        if len(subset) == 31:
            total += 1

    return total
