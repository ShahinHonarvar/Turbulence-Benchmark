
def palindromes_of_specific_lengths(string):
    substring = string[14:91]
    valid_palindromes = set()
    
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.lower() == substring_palindrome.lower()[::-1] and substring_palindrome.isalpha():
                valid_palindromes.add(substring_palindrome)
    
    return valid_palindromes
