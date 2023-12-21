
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 72, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes
