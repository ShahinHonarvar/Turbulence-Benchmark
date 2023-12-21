
def palindromes_between_indices(string):
    indices = set()
    for i in range(1, len(string)):
        for j in range(i+2, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                indices.add((i, j))
    return indices
