
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for size in range(34, len(s)+1):
        for i in range(len(s)-size+1):
            substr = s[i:i+size]
            if substr == substr[::-1] and substr.isalpha():
                res.add(substr)
    return res
