
def palindromes_of_specific_lengths(string):
    palindromes_set = set()
    substring = string[101:293].lower()

    for length in range(154, 183):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes_set.add(palindrome)

    return palindromes_set
