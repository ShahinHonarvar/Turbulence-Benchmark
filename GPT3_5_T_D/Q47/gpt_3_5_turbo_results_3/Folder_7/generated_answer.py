
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(104, 124):
        substr = string[119:257].lower()
        for i in range(0, len(substr) - length + 1):
            palindrome = substr[i:i+length]
            if palindrome.isalpha() and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
