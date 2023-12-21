
def palindromes_between_indices(s):
    import itertools
    import string
    
    english_letters = set(string.ascii_letters)
    letters_in_range = set(s[:8]).intersection(english_letters)
    palindromes = set()
    
    for perm in itertools.permutations(letters_in_range, 8):
        word = ''.join(perm).lower()
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
