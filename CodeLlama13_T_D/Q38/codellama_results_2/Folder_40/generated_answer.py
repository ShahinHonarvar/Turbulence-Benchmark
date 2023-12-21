
def find_subset_of_length_n(elements, n):
    return sum(1 << i for i in range(len(elements)) if bin(i).count('1') == n)
