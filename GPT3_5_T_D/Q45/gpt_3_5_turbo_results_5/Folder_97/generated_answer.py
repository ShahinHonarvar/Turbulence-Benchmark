
def palindromes_between_indices(string):
    import itertools
    import string
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    letters = string.ascii_letters
    subsets = set(itertools.permutations(string[:5], 5))
    palindromes = set()
    
    for subset in subsets:
        for perm in itertools.permutations(subset):
            pal = "".join(perm)
            if is_palindrome(pal) and len(pal) >= 3:
                palindromes.add(pal)
    
    return palindromes
