
def palindrome_of_length_n(s):
    s = "".join(c for c in s if c.isalpha())
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 256):
        substring = s[i:i+257]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
