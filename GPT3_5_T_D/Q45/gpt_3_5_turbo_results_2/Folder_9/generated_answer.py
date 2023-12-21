
def palindromes_between_indices(string):
    from itertools import permutations
    
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters = sorted(english_letters[:7])
    
    palindromes = set()
    
    for perm in permutations(english_letters, 7):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
