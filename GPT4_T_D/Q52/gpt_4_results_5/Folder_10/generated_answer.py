
def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    
    for l in range(len(s) - 53):
        substr = s[l : l + 54]
        if substr == substr[::-1] and substr.isalpha():
            res.add(substr)
    
    return res
