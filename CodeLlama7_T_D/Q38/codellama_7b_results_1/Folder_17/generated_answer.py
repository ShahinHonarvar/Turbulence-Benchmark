
def find_subset_of_length_n(set):
    return len(powerset(set))

def powerset(set):

    result = []

    for i in range(1 << len(set)):

        subset = []

        for j in range(len(set)):

            if i & (1 << j):

                subset.append(set[j])

        result.append(subset)

    return result
