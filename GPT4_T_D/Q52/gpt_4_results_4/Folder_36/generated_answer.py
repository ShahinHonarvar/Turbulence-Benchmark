
def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 338 + 1):
        sub_s = s[i:i+338]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            palindrome_set.add(sub_s)
    return palindrome_set
