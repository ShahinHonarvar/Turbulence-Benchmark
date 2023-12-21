
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 72):
        sub_s = s[i: i+73]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            result.add(sub_s)
    return result
