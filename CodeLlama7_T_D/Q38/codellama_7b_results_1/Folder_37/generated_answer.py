
def find_subset_of_length_n(my_set):
    n = len(my_set)
    total_subsets = 0
    for i in range(1 << n):
        binary_string = bin(i)[2:]
        binary_string = '0' * (n - len(binary_string)) + binary_string
        subset = set()
        for j, bit in enumerate(reversed(binary_string)):
            if bit == '1':
                subset.add(my_set[j])
        if len(subset) == 28:
            total_subsets += 1

    return total_subsets
