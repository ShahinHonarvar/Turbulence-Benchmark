
def find_subset_of_length_n(elements):
    subsets = []
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            for k in range(j+1, len(elements)):
                subsets.append((elements[i], elements[j], elements[k]))
    return len(subsets)
