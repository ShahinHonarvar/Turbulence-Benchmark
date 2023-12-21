
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    palindrome_set = set()
    for i in range(len(s) - 66):
        substring = s[i:i+67]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
