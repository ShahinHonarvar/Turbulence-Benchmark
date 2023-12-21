
def find_subset_of_length_n(s):
    count = 0
    for i in range(1 << len(s)):
        subset = []
        for j in range(len(s)):
            if (i >> j) & 1:
                subset.append(s[j])
        if len(subset) == 31:
            count += 1

    return count
