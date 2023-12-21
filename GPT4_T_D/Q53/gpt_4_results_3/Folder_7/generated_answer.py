
def palindrome_of_length_at_least_n(s):
    import re
    s = s.lower()
    palindromes = set()
    # removing non-english letters
    s = re.sub("[^a-z]", "", s)
    for i in range(len(s)):
        for j in range(i + 122, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
