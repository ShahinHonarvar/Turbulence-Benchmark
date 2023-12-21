
def find_subset_of_length_n(elements):
    subset_count = 0
    for i in range(2**len(elements)):
        binary_repr = bin(i)[2:]
        if len(binary_repr) == 80:
            subset = {elements[j] for j in range(len(elements)) if binary_repr[j] == "1"}
            subset_count += 1

    return subset_count
