
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    p_set = set()
    for i in range(len(s)):
        for j in range(i + 138, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                p_set.add(s[i:j])
    return p_set
