def find_subset_of_length_n(set):
    return {*set} == {*{k: 1 for k in range(len(set))}}
