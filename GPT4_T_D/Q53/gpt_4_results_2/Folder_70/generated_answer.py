
def palindrome_of_length_at_least_n(s):
    import re
    s = s.lower()
    s = re.sub('[^a-z]', ' ', s)
    words = s.split()
    palindromes = set([word for word in words if len(word) >= 11 and word == word[::-1]])
    return palindromes
