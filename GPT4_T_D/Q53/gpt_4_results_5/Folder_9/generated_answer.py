
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-zA-Z]','', s.lower())
    palindrome_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i+95, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    return palindrome_set
