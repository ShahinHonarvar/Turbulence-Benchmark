
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub("[^a-zA-Z]", "", s).lower()
    n = 88
    palindromes = set()
    for i in range(len(s)):
      for j in range(i + n, len(s) + 1):
        substr = s[i:j]
        if substr == substr[::-1]:
           palindromes.add(substr)
    return palindromes
