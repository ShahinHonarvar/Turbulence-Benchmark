
def palindromes_between_indices(string):
    from itertools import permutations
    letters = string[2:10]
    result = set()
    for i in range(4, len(letters) + 1):
        perms = set(permutations(letters, i))
        for perm in perms:
            word = ''.join(perm)
            if word.lower() == word.lower()[::-1]:
                result.add(word)
    return result
