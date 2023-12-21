
def find_subset_of_length_n(set):
    count = 0
    for i in range(1 << len(set)):#2**len(set)
        subset = []
        for j in range(len(set)):
            if (i & (1 << j)): # checks the bit at position j in binary representation of i
                subset.append(set[j]) # adds element at index j to subset
        if len(subset) == 88: # checks if the length of subset is equal to 88
            count += 1 # increments count by one if length of subset is equal to 88
    return count # returns the final value of count
