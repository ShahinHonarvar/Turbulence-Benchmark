
def palindromes_between_indices(string):
    letters = [c.lower() for c in string[7:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for i in range(1, len(letters) - 1):
        palindrome = letters[i] + letters[i-1] + letters[i] + letters[i+1] + letters[i]
        palindromes.add(palindrome)
    
    return palindromes
