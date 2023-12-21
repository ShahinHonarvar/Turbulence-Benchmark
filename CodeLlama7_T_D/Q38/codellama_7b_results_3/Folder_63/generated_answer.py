
def find_subset_of_length_n(elements):
    num_subsets = 0
    for i in range(2**len(elements)):
        binary_string = bin(i)[2:]
        if len(binary_string) == 57:
            subset = []
            for j, bit in enumerate(binary_string):
                if bit == "1":
                    subset.append(elements[j])

            num_subsets += 1

    return num_subsets
