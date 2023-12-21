
def palindromes_between_indices(string):
    letters = [c.lower() for c in string[7:9] if c.isalpha()]
    if len(letters) < 2:
        return set()
    
    palindromes = set()
    for i in range(len(letters)-1):
        for j in range(i+1, len(letters)):
            palindrome = ''.join(letters[i:j+1]) + ''.join(reversed(letters[i:j]))
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
