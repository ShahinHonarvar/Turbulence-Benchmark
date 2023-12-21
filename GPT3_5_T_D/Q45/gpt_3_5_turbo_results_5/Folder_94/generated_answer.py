
def palindromes_between_indices(string):
    import itertools
    
    letters = [letter.lower() for letter in string[3:5] if letter.isalpha()]
    
    all_palindromes = set()
    
    for arrangement in itertools.permutations(letters):
        palindrome = ''.join(arrangement)
        if palindrome == palindrome[::-1] and len(palindrome) >= 3:
            all_palindromes.add(palindrome)
    
    return all_palindromes
