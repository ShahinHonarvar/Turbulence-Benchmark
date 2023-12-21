
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:61].lower()

    for length in range(16, 40):
        for start in range(len(substring) - length + 1):
            substring_palindrome = substring[start:start+length]
            if substring_palindrome == substring_palindrome[::-1] and substring_palindrome.isalpha():
                palindromes.add(substring_palindrome)
    
    return palindromes
