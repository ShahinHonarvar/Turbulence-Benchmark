
def palindromes_between_indices(string):
    import itertools
    
    english_letters = [char for char in string if char.isalpha()]
    english_letters_lower = [char.lower() for char in english_letters]
    
    palindrome_set = set()
    
    for letters in itertools.permutations(english_letters_lower[:8], 8):
        if letters == letters[::-1]:
            palindrome_set.add("".join(letters))
    
    return palindrome_set
