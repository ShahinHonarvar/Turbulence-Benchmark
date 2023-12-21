
def palindromes_of_specific_lengths(s):
    import re
    s = s[0:301].lower()
    s = re.sub('[^a-z]', '', s)
    palindrome_set = set()
    for i in range(len(s) - 49):
        for j in range(i + 50, min(i + 61, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindrome_set.add(substr)
    return palindrome_set
