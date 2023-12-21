
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[31:92]
    
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.lower() == substring_palindrome[::-1].lower():
                palindromes.add(substring_palindrome)
    
    return palindromes
