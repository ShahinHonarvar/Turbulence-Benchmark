
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    length = len(s)
    palindrome_set = set()
    for i in range(length):
        for j in range(i+85, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    return palindrome_set
