
def find_subset_of_length_n(set, n):
    return len([i for i in range(1 << len(set)) if bin(i).count('1') == n])
