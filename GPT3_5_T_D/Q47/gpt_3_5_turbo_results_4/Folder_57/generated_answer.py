
def palindromes_of_specific_lengths(string):
    substring = string[16:95]
    palindromes = set()

    for length in range(39, 53):
        for start in range(len(substring) - length + 1):
            substring_palindrome = substring[start:start + length]
            if substring_palindrome.lower() == substring_palindrome.lower()[::-1]:
                palindromes.add(substring_palindrome)

    return palindromes
