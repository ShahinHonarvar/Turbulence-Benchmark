
def palindrome_of_length_n(s):
    s = s.lower()
    n = 420
    result = set()
    for i in range(len(s)):
        if i + n > len(s):
            break
        substring = s[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
