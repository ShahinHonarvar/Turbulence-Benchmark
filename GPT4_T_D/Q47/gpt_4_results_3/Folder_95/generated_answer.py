
def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindrome_set = set()
    for i in range(len(s)):
        for length in range(20, 22):
            if i+length > len(s):
                continue
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
