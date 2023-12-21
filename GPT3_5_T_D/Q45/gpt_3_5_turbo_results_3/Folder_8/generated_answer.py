
def palindromes_between_indices(string):
    import itertools
    import string as alphabets
    
    letters = ''
    for char in string:
        if char in alphabets.ascii_letters:
            letters += char.lower()
    
    palindromes = set()
    
    for arrangement in itertools.permutations(letters[1:6], 5):
        word = ''.join(arrangement)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    
    return palindromes
