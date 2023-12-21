
def palindromes_of_specific_lengths(string):
    import re
    string = string[12:93].lower()
    result = set()
    for i in range(42, 78):
        pattern = rf"(?i)([a-z]{{{i // 2}}})([a-z])?({''.join(reversed(string))}|{string})"
        matches = re.findall(pattern, string)
        for match in matches:
            palindrome = match[0] + (match[1] or '') + match[0][::-1]
            result.add(palindrome)
    return result
