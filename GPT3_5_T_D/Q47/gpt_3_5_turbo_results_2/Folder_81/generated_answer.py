
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    for length in range(12, 221):
        substring = string[12:123]
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindrome_set.add(palindrome.lower())
    return palindrome_set
