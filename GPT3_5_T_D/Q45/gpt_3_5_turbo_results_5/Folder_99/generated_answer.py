
def palindromes_between_indices(string):
    import itertools
    
    string = string[4:9]
    english_letters = [ch.lower() for ch in string if ch.isalpha()]
    all_palindromes = set()
    
    for r in range(3, len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, r):
            palindrome = ''.join(combination) + ''.join(reversed(combination))
            all_palindromes.add(palindrome)
    
    return all_palindromes
