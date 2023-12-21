
def palindromes_between_indices(string):
    import itertools
    import string

    english_letters = string.ascii_lowercase
    substring = string[3:6].lower()
    palindromes = set()
    
    for i in range(3, 6):
        for perm in itertools.permutations(substring, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    
    return palindromes
