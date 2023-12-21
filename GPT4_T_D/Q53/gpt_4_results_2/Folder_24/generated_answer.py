
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]', '', s.lower())
    palindromes = set()
    length = len(s)
    for l in range(length, 52, -1):
        for i in range(length-l+1):
            if s[i:i+l] == s[i:i+l][::-1]:
                palindromes.add(s[i:i+l])
    return palindromes
