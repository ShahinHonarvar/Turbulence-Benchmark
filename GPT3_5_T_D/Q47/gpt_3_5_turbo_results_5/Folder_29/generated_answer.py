
def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    palindromes = set()

    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start+length]
            if palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)

    return palindromes
