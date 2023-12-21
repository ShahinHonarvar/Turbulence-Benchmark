
def find_subset_of_length_n(set_of_elements):
    count = 0
    for i in range(len(set_of_elements)):
        for j in range(i+1, len(set_of_elements)):
            for k in range(j+1, len(set_of_elements)):
                # continue creating nested loops up to n-1 levels
                .
                .
                .
                # until the last level, add 1 to the count
                count += 1
    return count
