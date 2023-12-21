
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+38, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    return palindrome_set
