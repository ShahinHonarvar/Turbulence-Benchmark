
def palindrome_of_length_n(s):
    s = s.lower()
    n = 9
    result = set()
    for i in range(len(s)-n+1):
        sub_s = s[i: i+n]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            result.add(sub_s)
    return result
