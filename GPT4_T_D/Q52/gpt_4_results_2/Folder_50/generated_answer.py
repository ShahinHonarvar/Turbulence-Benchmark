
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if i+40 > len(s):
            break
        substring = s[i: i+40]
        if substring == substring[::-1]:
            if substring.isalpha():
                result.add(substring)
    return result
