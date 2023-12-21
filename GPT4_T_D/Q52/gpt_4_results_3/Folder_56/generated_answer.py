
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 95, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
