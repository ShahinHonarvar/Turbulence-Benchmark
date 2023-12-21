
def palindromes_of_specific_lengths(s):
    result = set()
    s = s[29:97]
    for length in range(12, 19):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                result.add(substr)
    return result
