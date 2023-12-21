
def palindromes_between_indices(s):
    return {i for i in s if len(i) >= 3 and i == i[::-1]}
