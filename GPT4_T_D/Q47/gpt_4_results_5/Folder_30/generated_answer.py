
def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[14:91]
    valid_chars = "abcdefghijklmnopqrstuvwxyz"
    s = ''.join([c for c in s if c in valid_chars])
    result = set()
    for i in range(len(s)):
        for j in range(i+55, min(i+72, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
