
def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 61, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                res.add(substr)
    return res
