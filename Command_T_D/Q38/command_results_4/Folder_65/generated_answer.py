def find_subset_of_length_n(s):
    return {i: {j: i.count(j) for j in s} for i in range(len(s) + 1)}
