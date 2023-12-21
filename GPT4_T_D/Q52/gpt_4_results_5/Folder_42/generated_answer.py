
def palindrome_of_length_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    result_set = set()
    for i in range(len(s)):
        for j in range(i + 279, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result_set.add(substring)
    return result_set
