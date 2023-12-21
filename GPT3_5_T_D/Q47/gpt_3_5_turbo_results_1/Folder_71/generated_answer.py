
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[18:66]
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome.isalpha() and palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
    return palindromes
