
def palindromes_of_specific_lengths(s):
    s = s[22:96]
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 52, min(i + 56, len(s) + 1)):
            part = s[i:j]
            if part == part[::-1]:
                result.add(part)
    return result
