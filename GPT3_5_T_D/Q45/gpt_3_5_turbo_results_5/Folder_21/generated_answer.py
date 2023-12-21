
def palindromes_between_indices(string):
    import itertools
    import re
    string = string.lower()
    letters = re.findall('[a-zA-Z]', string[1:9])
    if len(letters) < 7:
        return set()
    else:
        palindromes = set()
        for perm in itertools.permutations(letters, len(letters)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
        return palindromes
