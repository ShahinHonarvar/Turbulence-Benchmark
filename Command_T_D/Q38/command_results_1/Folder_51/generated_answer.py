def find_subset_of_length_n(s):
    return sum(0 < x < y < len(s) for x, y in zip(range(len(s)), range(x, y + 1, len(s))))
