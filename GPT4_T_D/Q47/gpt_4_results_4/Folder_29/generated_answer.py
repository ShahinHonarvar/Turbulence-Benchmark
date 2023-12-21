
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:95]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    result = set()
    for length in range(18, 74):
        for start in range(len(s)-length+1):
            substring = s[start:start+length]
            if substring == substring[::-1]:
                result.add(substring)
    return result
