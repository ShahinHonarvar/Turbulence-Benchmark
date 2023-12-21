
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    res = set()
    for length in range(22, len(s)+1):
        for start in range(0, len(s)-length+1):
            substring = s[start:start+length]
            if substring == substring[::-1]:
                res.add(substring)
    return res
