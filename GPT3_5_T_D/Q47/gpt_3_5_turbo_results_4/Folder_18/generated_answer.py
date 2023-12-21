
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:84].lower()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes
