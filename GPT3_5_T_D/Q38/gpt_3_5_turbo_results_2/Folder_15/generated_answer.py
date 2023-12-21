
def find_subset_of_length_n(elements):
    n = 10
    count = 0
    if len(elements) < n:
        return count
    else:
        for i in range(len(elements) - n + 1):
            count += 1
    return count
