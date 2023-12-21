
def palindromes_between_indices(string):
    return set([i[::-1] for i in string[2:3]])
