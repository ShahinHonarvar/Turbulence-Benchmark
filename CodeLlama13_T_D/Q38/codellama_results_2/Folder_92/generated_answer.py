
def find_subset_of_length_n(elements, n):
    return len([i for i in range(1 << n) if bin(i)[2:] == ''.join('1' if j in elements else '0' for j in range(n))])
