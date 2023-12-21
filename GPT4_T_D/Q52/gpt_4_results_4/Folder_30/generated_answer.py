
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 == 94:
                substring = s[i:j+1]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result
