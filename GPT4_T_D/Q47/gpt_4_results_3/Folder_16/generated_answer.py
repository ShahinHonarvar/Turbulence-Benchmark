
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:87]
    result = set()
    for length in range(51, 61):
        for start in range(len(s)-length+1):
            substring = s[start:start+length]
            if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
                result.add(substring.lower())
    return result
