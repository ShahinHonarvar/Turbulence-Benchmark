
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 96):
        substring = s[i:i+97]
        if all(c.isalpha() for c in substring) and substring == substring[::-1]:
            result.add(substring)
    return result
