
def palindromes_of_specific_lengths(string):
    substring = string[26:91].lower()
    palindromes = set()
    
    for length in range(27, 59):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    
    return palindromes
