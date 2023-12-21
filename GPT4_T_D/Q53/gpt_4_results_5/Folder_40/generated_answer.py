
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    p_set = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                p_set.add(sub)
    return p_set
