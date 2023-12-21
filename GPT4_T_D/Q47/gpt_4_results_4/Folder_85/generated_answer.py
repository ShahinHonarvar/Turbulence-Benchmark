
def palindromes_of_specific_lengths(s):
    import re
    s = s[29:99].lower()
    s = re.sub('[^a-z]', '', s)
    results = set()
    for i in range(len(s)):
        for j in range(i + 6, min(i + 10, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                results.add(substring)
    return results
