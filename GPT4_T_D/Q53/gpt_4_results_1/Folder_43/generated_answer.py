
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+49, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
