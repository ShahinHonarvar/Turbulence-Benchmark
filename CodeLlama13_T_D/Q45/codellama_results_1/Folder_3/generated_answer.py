
def palindromes_between_indices(string):
    indices = set()
    for i in range(7, 10):
        for j in range(i + 2, len(string)):
            if string[i:j] == string[j - (i + 2):j][::-1]:
                indices.add(string[i:j])
    return indices
