
def palindrome_of_length_at_least_n(s):
    import re
    s = s.lower()
    s = re.sub('[^a-z]', '', s)

    palindromes = set()
    l = len(s)

    for i in range(l):
        for j in range(i + 140, l + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)

    return palindromes
