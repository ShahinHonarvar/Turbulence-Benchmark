
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:94]
    for length in range(34, 55):
        for index in range(len(substring) - length):
            substring_palindrome = substring[index:index+length]
            if substring_palindrome.isalpha() and substring_palindrome.lower() == substring_palindrome.lower()[::-1]:
                palindromes.add(substring_palindrome)
    return palindromes
