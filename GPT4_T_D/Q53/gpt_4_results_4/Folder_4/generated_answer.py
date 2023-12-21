
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^A-Za-z]', '', s).lower()
    palindromes = set()
    length = len(s)

    for i in range(length):
        for j in range(i+99, length+1):
            snippet = s[i:j]
            if snippet == snippet[::-1]:
                palindromes.add(snippet)
    return palindromes
