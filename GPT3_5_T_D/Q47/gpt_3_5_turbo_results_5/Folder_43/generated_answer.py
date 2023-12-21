
def palindromes_of_specific_lengths(string):
    substring = string[41:90]
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.lower() == substring_palindrome.lower()[::-1] and substring_palindrome.isalpha():
                palindromes.add(substring_palindrome)
    return palindromes
