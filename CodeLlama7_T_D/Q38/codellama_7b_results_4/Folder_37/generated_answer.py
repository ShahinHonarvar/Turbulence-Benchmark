
def find_subset_of_length_n(my_set):
    n = len(my_set)
    total = 1
    for i in range(28, n + 1):
        total *= i

    return total
