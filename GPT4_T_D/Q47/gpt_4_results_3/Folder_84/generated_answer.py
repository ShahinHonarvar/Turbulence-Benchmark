
def palindromes_of_specific_lengths(s):
    import re
    s = re.sub('[^a-z]+', '', s.lower())
    s = s[23:78]
    result = set()
    for i in range(len(s)):
        for j in range(i+13, min(i+41, len(s)+1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result
