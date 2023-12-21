
def palindromes_of_specific_lengths(string):
    substring = string[40:95]
    palindromes = set()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.lower() == substring_palindrome.lower()[::-1]:
                if substring_palindrome.isalpha():
                    palindromes.add(substring_palindrome)
    return palindromes
