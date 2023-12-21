
def palindromes_between_indices(string):
    import itertools
    
    # Extract the English letters from the given string between index 1 and index 7
    substring = ''.join([ch for ch in string[1:8] if ch.isalpha()])
    
    # Generate all possible arrangements of the English letters
    arrangements = set(''.join(chars) for chars in itertools.permutations(substring.lower()))
    
    # Filter and return the palindromes of length at least 3
    palindromes = {word for word in arrangements if len(word) >= 3 and word == word[::-1]}
    
    return palindromes
