
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    letters = Counter(string[7:10].lower())
    permutations = set(itertools.permutations(letters.elements()))
    
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 4:
            palindromes.add(palindrome)
    
    return palindromes
