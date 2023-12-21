
def palindromes_of_specific_lengths(s):
    s = s[1:10]
    s = s.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    s = ''.join(c for c in s if c in valid_chars)
    palindrome_set = set()
    for i in range(3,8):
        for j in range(len(s)-i+1):
            substring = s[j:j+i]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
