
def palindromes_between_indices(string):
    import itertools
    import re
    
    letters = re.findall('[a-zA-Z]', string[3:8])
    if len(letters) < 5:
        return set()
    
    palindromes = set()
    for permutation in itertools.permutations(letters, 5):
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
