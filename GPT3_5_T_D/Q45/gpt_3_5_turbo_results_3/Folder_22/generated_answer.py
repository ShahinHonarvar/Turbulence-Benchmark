
def palindromes_between_indices(string):
    import itertools
    
    english_letters = ""
    for char in string[5:7]:
        if char.isalpha():
            english_letters += char
    
    permutations = set()
    for permutation in itertools.permutations(english_letters.lower()):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            permutations.add(palindrome)
    
    return permutations
