
def find_subset_of_length_n(s):
    n = 13
    count = 0
    for i in range(len(s)):
        count += len(s) - i
    return count
