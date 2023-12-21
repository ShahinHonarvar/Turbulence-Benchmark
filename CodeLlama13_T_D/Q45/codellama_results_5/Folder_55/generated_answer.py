
def palindromes_between_indices(string):
    indices = set()
    for i in range(len(string) - 2):
        if string[i] == string[i + 1]:
            indices.add(i)
    return {string[i:i + 3] for i in indices}
