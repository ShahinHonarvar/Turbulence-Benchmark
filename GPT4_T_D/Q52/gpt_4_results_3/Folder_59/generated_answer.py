
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+39, len(s)+1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result
