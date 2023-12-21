
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes_set = set()
    for i in range(75, 96):
        for palindrome_length in range(7, 10):
            if i + palindrome_length > 96:
                break
            palindrome = string[i:i+palindrome_length]
            if palindrome.isalpha() and palindrome == palindrome[::-1]:
                palindromes_set.add(palindrome)
    return palindromes_set
