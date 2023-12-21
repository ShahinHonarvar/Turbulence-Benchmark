
def palindromes_between_indices(string):
    from itertools import permutations
    import re
    
    letters = ''.join(re.findall('[a-zA-Z]', string[5:8])).lower()
    
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if len(palindrome) >= 4 and palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
