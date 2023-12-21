
def palindrome_of_length_n(s):
    s = s.lower()
    len_s = len(s)
    palindrome_set = set()
    for i in range(len_s):
        for j in range(i+84, len_s+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
