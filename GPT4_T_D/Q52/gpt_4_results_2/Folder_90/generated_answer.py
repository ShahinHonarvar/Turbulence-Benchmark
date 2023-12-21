
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        if i + 318 > len(s):
            break
        substring = s[i:i+318]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
