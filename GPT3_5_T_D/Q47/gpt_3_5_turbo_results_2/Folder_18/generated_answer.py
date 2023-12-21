
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:84].lower()
    
    for length in range(13, 67):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    
    return palindromes
