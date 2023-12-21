
def palindromes_between_indices(string):
    import itertools
    import string
    
    english_letters = set(string.ascii_letters)
    palindrome_set = set()
    
    for combination in itertools.combinations(string[2:9], 6):
        combination = ''.join(combination).lower()
        if combination == combination[::-1]:
            palindrome_set.add(combination)
    
    return palindrome_set
