
def palindromes_between_indices(string):
    from itertools import permutations
    string = string.lower()
    letters = [c for c in string[:6] if c.isalpha()]
    palindromes = set()
    
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
