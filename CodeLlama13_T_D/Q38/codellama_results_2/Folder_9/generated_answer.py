
def find_subset_of_length_n(elements):
    return len([i for i in range(len(elements) + 1) if bin(i).count('1') == n])
