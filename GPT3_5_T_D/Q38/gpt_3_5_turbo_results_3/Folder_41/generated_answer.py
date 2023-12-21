
def find_subset_of_length_n(elements):
    count = 0
    for i in range(len(elements)):
        if len(elements[i]) == 84:
            count += 1
    return count
