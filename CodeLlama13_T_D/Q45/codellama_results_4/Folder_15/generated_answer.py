
def palindromes_between_indices(string):
    return set([word[::-1] for word in string.split() if len(word) >= 3 and all([i == j for i, j in zip(word, word[::-1])])])
