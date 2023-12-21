
def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    if len(letters) < 6:
        return set()
    
    palindromes = set()
    for i in range(3, 6):
        for j in range(i, 6):
            palindrome = ''.join(letters[i:j+1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
