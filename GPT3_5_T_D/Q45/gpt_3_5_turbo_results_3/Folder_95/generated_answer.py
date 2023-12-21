
def palindromes_between_indices(string):
    import itertools
    import re

    letters = re.findall('[a-zA-Z]', string[7:9])
    letter_permutations = itertools.permutations(letters)
    palindromes = set()
    
    for permutation in letter_permutations:
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            palindromes.add(palindrome)
            
    return palindromes
