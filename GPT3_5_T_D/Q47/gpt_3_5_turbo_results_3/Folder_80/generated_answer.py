
def palindromes_of_specific_lengths(string):
    palindromes = set()

    substring = string[35:89].lower()

    for length in range(24, 34):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)

    return palindromes
