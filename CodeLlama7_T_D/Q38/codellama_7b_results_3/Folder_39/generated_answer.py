
def find_subset_of_length_n(elements):
    n = len(elements)
    if n == 0:
        return 1

    else:

        return (find_subset_of_length_n(elements[:-1])) * (n + 1)
