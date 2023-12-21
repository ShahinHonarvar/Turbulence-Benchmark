
def palindromes_between_indices(string):
    import itertools

    letters = []
    for char in string[:8]:
        if char.isalpha():
            letters.append(char)
    
    permuted_letters = set(itertools.permutations(letters, 8))
    palindromes = set()
    
    for permutation in permuted_letters:
        word = ''.join(permutation)[:6]
        if word.lower() == word[::-1].lower():
            palindromes.add(word.lower())
    
    return palindromes
