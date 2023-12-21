
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters
    
    substring = string[6:9].lower()
    english_letters = ''.join(filter(str.isalpha, string.lower()))
    
    palindromes = set()
    for perm in itertools.permutations(english_letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
