
def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[155:284]
    palindromes = set()

    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]

            if substring_palindrome.isalpha() and substring_palindrome == substring_palindrome[::-1]:
                palindromes.add(substring_palindrome)

    return palindromes
