
def find_subset_of_length_n(set):
    # Calculate the number of subsets for a set of size n
    total = 1
    for i in range(1, len(set)):
        total += (total * (len(set) - i)) / (i + 1)
    return total
