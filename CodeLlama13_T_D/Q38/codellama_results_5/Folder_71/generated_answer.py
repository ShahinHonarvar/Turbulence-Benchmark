
def find_subset_of_length_n(elements):
    return len([i for i in range(2**len(elements)) if bin(i).count('1') == 78])
