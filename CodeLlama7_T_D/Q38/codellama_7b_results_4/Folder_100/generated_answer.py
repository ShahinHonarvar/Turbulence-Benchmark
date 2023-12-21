
def find_subset_of_length_n(set):
    def subset_count(n, set):
        return 2 ** (len(set) - n)

    return sum(subset_count(99, set))
