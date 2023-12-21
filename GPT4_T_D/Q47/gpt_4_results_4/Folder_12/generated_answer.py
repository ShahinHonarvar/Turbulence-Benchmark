
def palindromes_of_specific_lengths(s):
    import re
    palindrome_set = set()
    s = s[62:89].lower()
    s = re.sub('[^a-z]', '', s)
    for i in range(len(s)):
        for j in range(i+18, min(i+22, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindrome_set.add(substr)
    return palindrome_set
