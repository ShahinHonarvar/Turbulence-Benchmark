
def find_subset_of_length_n(elements):
    count = 0
    if len(elements) < 76:
        return count
    subset_count = 2 ** len(elements)
    for i in range(subset_count):
        if bin(i).count('1') == 76:
            count += 1
    return count
