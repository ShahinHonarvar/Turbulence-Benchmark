
def palindromes_between_indices(string):
    import itertools
    import string as s
    
    palindromes = set()
    
    for combination in itertools.permutations(string[3:9], 6):
        palindrome = ''.join(combination).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 5 and any(char.isalpha() for char in palindrome):
            palindromes.add(palindrome)
    
    return palindromes
