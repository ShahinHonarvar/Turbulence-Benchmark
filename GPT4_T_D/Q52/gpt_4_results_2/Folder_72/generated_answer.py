
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(0, len(s) - 15):
        substring = s[i:i+16]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
