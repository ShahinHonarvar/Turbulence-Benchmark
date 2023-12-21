
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    palindromes = set()
    letters = [c.lower() for c in string[3:7] if c.isalpha()]
    letter_counts = Counter(letters)
    
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
