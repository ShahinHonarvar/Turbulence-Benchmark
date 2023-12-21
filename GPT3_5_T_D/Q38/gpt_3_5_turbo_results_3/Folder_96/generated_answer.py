
def find_subset_of_length_n(elements):
    n = 47
    count = 0
    for i in range(1 << len(elements)):
        if bin(i).count('1') == n:
            count += 1
    return count
