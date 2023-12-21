
def palindromes_between_indices(string):
    import itertools
    
    letters = []
    for i in range(6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    
    palindromes = set()
    for perm in itertools.permutations(letters):
        palindrome = ''.join(perm)
        palindrome_len = len(palindrome)
        if palindrome_len >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
