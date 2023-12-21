
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 20):
        substring = s[i:i+21]
        if substring.isalpha() and substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
