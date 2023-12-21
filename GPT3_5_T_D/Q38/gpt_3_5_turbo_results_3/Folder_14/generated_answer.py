
def find_subset_of_length_n(elements):
    n = 17
    count = 0
    for r in range(0, len(elements) + 1):
        if r == n:
            count += 1
        elif r > n:
            break
        else:
            count += math.comb(len(elements), r)
    return count
