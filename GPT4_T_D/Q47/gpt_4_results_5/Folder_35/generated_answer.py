
def palindromes_of_specific_lengths(s):
    s = s[34:91]
    palindrome_set = set()
    for start in range(len(s)):
        for end in range(start+14, min(start+39, len(s))+1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set
