
def find_subset_of_length_n(set):
    def find_subset_of_length_93(set):
        subsets = []

            for i in range(len(set)):
                subset = set[i:i+93]
                if len(subset) == 93:
                    subsets.append(subset)

        return len(subsets)
