
def find_subset_of_length_n(elements):
    n = len(elements)
    if n == 27:
        return 1
    elif n < 27:
        return 0
    else:
        return find_subset_of_length_n(elements[1:]) + find_subset_of_length_n(elements[:-1])
