
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:99]
    s = re.sub("[^a-zA-Z]", "", s)
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i +31, min(i + 52, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                results.add(s[i:j])
    return results
