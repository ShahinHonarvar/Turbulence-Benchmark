
def palindromes_between_indices(string):
    import itertools
    
    letters = []
    for letter in string[2:8]:
        if letter.isalpha():
            letters.append(letter.lower())
    
    palindromes = set()
    for permutation in itertools.permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
