
def palindromes_between_indices(string):
    import itertools
    import string
    
    english_letters = set(string.ascii_letters)
    letters_in_range = [char.lower() for char in string[:7] if char.lower() in english_letters]
    
    if len(letters_in_range) < 3:
        return set()
    
    palindromes = set()
    for permutation in itertools.permutations(letters_in_range, len(letters_in_range)):
        word = ''.join(permutation)
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    
    return palindromes
