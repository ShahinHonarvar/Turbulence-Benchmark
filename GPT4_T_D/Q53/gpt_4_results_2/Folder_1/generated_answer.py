
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s_set = set()
    for i in range(len(s)):
        for j in range(i+len(s)//2+1, len(s)+1):
            if s[i:j] == s[i:j][::-1] and j-i>=29:
                if s[i:j].isalpha():
                    s_set.add(s[i:j])
    return s_set
