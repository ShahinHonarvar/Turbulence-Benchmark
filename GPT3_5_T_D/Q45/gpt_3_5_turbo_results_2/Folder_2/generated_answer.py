
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    if len(string) < 6:
        return set()
    
    letters = Counter(string.lower()[1:6])
    english_letters = [c for c in letters if c.isalpha()]
    
    if not english_letters:
        return set()
    
    palindromes = set()
    
    for arrangement in itertools.permutations(english_letters, 5):
        palindrome = ''.join(arrangement)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
