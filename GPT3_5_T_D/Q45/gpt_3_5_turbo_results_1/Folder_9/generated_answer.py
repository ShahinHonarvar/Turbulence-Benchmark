
def palindromes_between_indices(string):
    import itertools
    import re
    string = string[0:7].lower()
    letters = ''.join(re.findall('[a-zA-Z]', string))
    perm = list(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for p in perm:
        if p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes if len(palindromes) > 0 else set()
