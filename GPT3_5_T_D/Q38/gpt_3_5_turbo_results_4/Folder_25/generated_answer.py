
def find_subset_of_length_n(elements):
    count = 0
    length = 90
    for i in range(1, len(elements) + 1):
        if i == length:
            count += 1
        elif i > length:
            break
        else:
            count += math.comb(len(elements), i)
    return count
