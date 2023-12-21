
def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    s = s[12:123]
    s = ''.join(filter(str.isalpha, s)).lower()
    
    for i in range(len(s)):
        for j in range(i + 12, min(i + 221, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
