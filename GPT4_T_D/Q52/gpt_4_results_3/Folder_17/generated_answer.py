
def palindrome_of_length_n(s):
    s = s.lower()
    l = len(s)
    res = set()
    for i in range(l):
        for j in range(i, l):
            if j - i + 1 == 289:
                substr = s[i:j+1]
                if substr == substr[::-1] and substr.isalpha():
                    res.add(substr)
    return res
