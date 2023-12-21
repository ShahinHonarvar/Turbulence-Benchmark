
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = 338
    for i in range(len(s) - length + 1):
        substring = s[i: i + length]
        if all(c.isalpha() for c in substring) and substring == substring[::-1]:
            result.add(substring)
    return result
