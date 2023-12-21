
def find_subset_of_length_n(elements):
    return sum(1 for i in range(1, 100) if len(set(elements).intersection({j*i for j in elements})) == 100)
