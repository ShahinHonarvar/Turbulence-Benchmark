
def find_subset_of_length_n(elements, n):
    if len(elements) == 0:
        return 1
    else:
        return sum([find_subset_of_length_n(elements[1:], n - 1) for _ in range(len(elements))])
