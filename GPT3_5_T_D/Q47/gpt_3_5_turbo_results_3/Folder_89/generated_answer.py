
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[18:89]
    substring = substring.lower()
    
    for i in range(len(substring)):
        for length in range(12, 15):
            if i + length > len(substring):
                break
            
            palindrome = substring[i:i+length]
            if palindrome.isalpha() and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
