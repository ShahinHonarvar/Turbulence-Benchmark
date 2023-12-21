
def find_subset_of_length_n(elements):
    count = 0
    n = 47
    for i in range(len(elements)):
        if len(elements[i]) == n:
            count += 1
    return count
