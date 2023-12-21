
def find_subset_of_length_n(set):
    count = 0
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            if (j - i) == 22:
                count += 1

    return count
