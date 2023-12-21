
def palindrome_of_length_at_least_n(s):
    s = "".join(c.lower() for c in s if c.isalpha())
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 115, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
